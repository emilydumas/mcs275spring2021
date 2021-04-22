-- MCS 275 Spring 2021 - David Dumas

-- SQLite command line shell commands to convert hygdata_v3.csv from
--     https://github.com/astronexus/HYG-Database/blob/master/hygdata_v3.csv?raw=true
-- to a sqlite3 database for use in MCS 275 problems.

-- The source CSV is part of the HYG database archive created by David Nash
-- and available under a CC license.  See http://www.astronexus.com/hyg


-- STEP 1: Create the table `stars`

-- This is necessary because if we directly import a CSV and let it create
-- a table, then every column will have type TEXT.

CREATE TABLE stars (
  id INTEGER PRIMARY KEY,
  hip INTEGER,
  hd INTEGER,
  hr INTEGER,
  gl TEXT,
  bf TEXT,
  proper TEXT,
  ra REAL,
  dec REAL,
  dist REAL,
  pmra REAL,
  pmdec REAL,
  rv REAL,
  mag REAL,
  absmag REAL,
  spect TEXT,
  ci REAL,
  x REAL,
  y REAL,
  z REAL,
  vx REAL,
  vy REAL,
  vz REAL,
  rarad REAL,
  decrad REAL,
  pmrarad REAL,
  pmdecrad REAL,
  bayer TEXT,
  flam INTEGER,
  con TEXT,
  comp INTEGER,
  comp_primary INTEGER,
  base TEXT,
  lum REAL,
  var TEXT,
  var_min REAL,
  var_max REAL
);

-- STEP 2: Import the CSV

-- Now configure for CSV importing and add the rows to
-- table `stars`.  These are not SQL commands, but SQLite
-- command line shell commands, which start with ".".

.separator ,
.header on
.import "hygdata_v3.csv" stars


-- STEP 3: Cleaning

-- Finally, search for empty string ("") values in columns and
-- replace them with null values.  (It turns out this search 
-- was not complete, and some empty string values remain in 
-- other columns.  But a database update after releasing the
-- associated course problem sets was not desirable.)

UPDATE stars SET gl=NULL WHERE gl="";
UPDATE stars SET bf=NULL WHERE bf="";
UPDATE stars SET proper=NULL WHERE proper="";
UPDATE stars SET spect=NULL WHERE spect="";
UPDATE stars SET bayer=NULL WHERE bayer="";
UPDATE stars SET con=NULL WHERE con="";
UPDATE stars SET base=NULL WHERE base="";
UPDATE stars SET var=NULL WHERE var="";
