"""Scraper to convert UIC academic calendar site to CSV"""
# MCS 275 Spring 2021 Lecture 41
# David Dumas

# This scraper converts the session calendar tables at
# https://catalog.uic.edu/ucat/academic-calendar/
# to a CSV file.  The tables contain two kinds of events:
#   * single date events, like "May 18, M. Instruction begins."
#   * date ranges, like "August 6-7, Th-F. Final examinations.""
# To represent either of these as a single row in the CSV output file, we
# include both a start date and end date for each event.  Single date events are
# then just events where start and end dates are equal.

# The calendar page also has a single table for the 4-week summer session and the
# 8-week summer session.  This scraper considers those to be separate sessions
# and marks them appropriately in the output file (as "summer4wk" and "summer8wk")

from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import sys
import csv
import datetime

def normalize_hyphens(s):
    """Take any hyphen, minus, or other dash-like unicode code point in `s` and
    replace with - (\u002D)"""
    dashlike = "֊־᠆‐‑‒–—―⁓⁻₋−⸺⸻〜〰゠﹘﹣－"  # adapted from https://jkorpela.fi/dashes.html
    for c in dashlike:
        s = s.replace(c,"-")
    return s

def parse_singledate(s,year):
    """Convert a string s like "January 13" and a year string
    like "2019" to a date object"""
    return datetime.datetime.strptime(
        s + " " + year,  # like "January 13 2020"
        "%B %d %Y" # month_name day_of_month year
    ).date()   # The final .date() converts from a datetime to a date

def parse_datespec(datespec,year):
    """Convert a date specification string like "January 13, M" or "November
    25–26, Th–F" to a pair of Python date objects representing the start and end
    of the date range.  Returned as a pair start_date, end_date."""
    # Discard the day of week info after the ,
    # TODO: Store the day of week info and use for data validation!
    datespec = datespec.split(",")[0]

    # UIC academic calendar uses proper dashes, not the minus sign
    # on most keyboards.  Let's convert all dashes to minus signs.
    datespec = normalize_hyphens(datespec)

    # If there is no "-" in datespec, it specifies a single date
    if "-" not in datespec:
        d = parse_singledate(datespec,year)
        return d,d

    # If we make it here, we're processing a string representing a date range.
    
    # Date ranges usually look like "January 18-21" but we should allow for the
    # possibility that a date range might span a month boundary.  I expect that
    # would be written similar to "February 28-March 2".  So after splitting
    # along - we know the first field is a month+day, and the second is either a
    # number or a month+day.

    # We also allow for use of multiple dashes, which would generate blank
    # strings in .split("-"), which we filter out here.
    startstr, endstr = [ x.strip() for x in datespec.split("-") if len(x)>0 ]
    
    # Now expect startstr like "January 18" and endstr like "21"
    #         OR startstr like "February 28" and endstr like "March 2"

    start_date = parse_singledate(startstr,year)
    if endstr.isnumeric():
        # End of range is just a number, so the end date reuses the month of
        # startstr.
        end_date = start_date.replace(day=int(endstr))
    else:
        # Range spans a month boundary; end of range not just a number, so we
        # consider it as month+day.
        end_date = parse_singledate(endstr,year)

    return start_date, end_date


# If argument provided, use it as the output filename.
outfn = "calimproved.csv"
if len(sys.argv)>1:
    outfn = sys.argv[1]

print("Waiting 10 seconds before actually retrieving the academic calendar")
print("from https://catalog.uic.edu/ucat/academic-calendar/")
print("(this is a rate limiter, to prevent frequent automated requests)")
time.sleep(10)

print("Fetching and parsing HTML")
with urlopen("https://catalog.uic.edu/ucat/academic-calendar/") as response:
    soup = BeautifulSoup(response,"html.parser")

print("Converting to CSV and saving to '{}'".format(outfn))

rowcount = 0
sessioncount = 0
with open(outfn,"wt",newline="") as outfobj:
    writer = csv.DictWriter(outfobj,fieldnames=["year","semester","start_date","end_date","description"])
    writer.writeheader()
    # The academic calendar site has many tables.  Each one lists events for
    # a session (semester or summer).  The session name appears in a h2 above
    # the table.
    for t in soup.find_all("table"):
        # t is a schedule table
        # look for the preceding h2 to get which session it shows
        session_name = t.find_previous_sibling("h2").text.lower()

        # now session_name is something like "fall semester 2021"
        # of "summer session 2021".  Split into three components.
        season, sessiontype, year = session_name.split()
        if sessiontype == "semester":
            # Fall or Spring
            semester = season
            sessioncount += 1
            print("Processing data for {} {}".format(semester,year))
        else:
            # Fill in later when we encounter table row for
            # 4- and 8-week summer data
            semester = None

        # Loop to examine rows of the semester table
        for r in t.find_all("tr"):
            if r.parent.name == "thead":
                # rows that appear inside thead tag are part of the table header,
                # not its content.
                continue
            datespec, desc = [ x.text for x in r.find_all("td") ]
            
            if semester not in ["fall","spring"]:
                # This is a summer session, so we don't know *which* session
                # until we read the row in the table indicating it. Check to see
                # if this is such a row. If so, change the value of semester,
                # which will apply to all rows below.
                s = normalize_hyphens(desc.lower())
                if "4-week session" in s:
                    semester = "summer4wk"
                    sessioncount += 1
                    print("Processing data for {} {}".format(semester,year))
                    continue
                elif "8-week session" in s:
                    semester = "summer8wk"
                    sessioncount += 1
                    print("Processing data for {} {}".format(semester,year))
                    continue
            
            if datespec:
                start_date, end_date = parse_datespec(datespec,year)

            # If datespec is blank, it means we are processing a second or
            # subsequent event that happens on the same day as a previous row in
            # the table.  (This happens e.g. with Jan 20, 2023, which is both a
            # holiday and a deadline.) The body of the if statement above is not
            # executed in this case, so start_date and end_date retain their
            # values from the previous row and we can just reuse them.

            # If semester is None at this point, something went wrong; we expect
            # to know *which* summer session we're looking at before we start
            # writing any summer events to the output file.
            assert semester is not None

            writer.writerow(
                {"semester":semester,
                 "year":int(year),
                 "start_date":str(start_date),
                 "end_date":str(end_date),
                 "description":desc
                }
            )
            rowcount += 1

print("Processed {} events for {} sessions.".format(rowcount,sessioncount))

# NOTE: It would be tempting to add more processing to this scraper, e.g. to try
# to categorize events as start and end of class, holidays, deadlines, other.
# However, I think that kind of processing belongs in a separate program that
# *uses* the data generated by this scraper.  It is usually best for a scraper
# to stop when it has the minimal unambiguous structured representation of the
# source data.

# NOTE: Rather than using CSV for storage, a more natural approach would be to
# use a database with two tables: One for scrapes, and one for scraped data.
# Each time the program is run, a new scrape is generated and given an integer
# id and timestamp in the `scrapes` table.  Then, the rows of event data are
# added to the `scraped_events` table, each of them tagged with the
# corresponding scrape id.  Then, a program using the scraped data could use SQL
# queries to retrieve:
#   * the most recent scrape
#   * the first scrape
#   * all scrapes that contain an event on a certain day
#   * all dates that appear in "Instruction begins." events
#   * event dates that appear in one scrape for a certain year+semester and not
#     another, indicating a change of schedule
#   * etc.
