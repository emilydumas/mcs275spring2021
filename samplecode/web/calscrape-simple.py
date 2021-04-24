"""Simple scraper to convert UIC academic calendar site to CSV"""
# MCS 275 Spring 2021 Lecture 41
# David Dumas

# This "simple" scraper looks for the table of dates for each Spring and Fall
# semester listed at
# https://catalog.uic.edu/ucat/academic-calendar/
# and writes them to a CSV file.  Any table entry that contains a date *range*
# is ignored.  Also, in Fall 2021 there is a single date with two corresponding
# events (a deadline and a holiday). The second event is ignored by this script
# because the table has an empty date next to it (expecting it to be clear that
# the date is the same as the previous row).

from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import sys
import csv
import datetime

def parse_datespec(datespec,year):
    """Take a date specification string like
    "January 13, M" and a year like "2020" and
    convert to a Python date object."""
    # Discard the day of week after the ,
    datespec = datespec.split(",")[0]
    return datetime.datetime.strptime(
        datespec + " " + year,  # like "January 13 2020"
        "%B %d %Y" # month_name day_of_month year
    ).date()   # The final .date() converts from a datetime to a date

# If argument provided, use it as the output filename.
outfn = "calsimple.csv"
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

with open(outfn,"wt",newline="") as outfobj:
    writer = csv.DictWriter(outfobj,fieldnames=["year","semester","date","description"])
    writer.writeheader()
    # The academic calendar site has many tables.  Each one lists events for
    # a session (semester or summer).  The session name appears in a h2 above
    # the table.
    for t in soup.find_all("table"):
        # t is a schedule table
        # look for the preceding h2 to get which session it shows
        session_name = t.find_previous_sibling("h2").text.lower()
        if "summer" in session_name:
            # This scraper doesn't handle summer
            continue
        # now session_name is something like "fall semester 2021"
        # want semester="fall" and year="2021"
        semester, _, year = session_name.split()

        # Loop to examine rows of the semester table
        for r in t.find_all("tr"):
            if r.parent.name == "thead":
                # rows that appear inside thead tag are part of the table header,
                # not its content.
                continue
            datespec, desc = [ x.text for x in r.find_all("td") ]
            # TODO: Handle ranges of dates.  For now, we just
            # skip the row if parsing gives an exception due
            # to the presence of a hyphen.
            try: 
                date = parse_datespec(datespec,year)
            except Exception:
                print("SKIPPING: ",datespec,desc)
                print("(probably contains a range of dates; this script only handles single dates)")
                continue
            writer.writerow(
                {"semester":semester,
                 "year":int(year),
                 "date":str(date),
                 "description":desc}
            )
