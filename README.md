# time-series-basics
Time Series basics - importing, cleaning, printing to csv

Note date files are synthetic data.
#data_import.py contains ImportData class. To use, you must first import the following:

```
import csv
import dateutil.parser
from os import listdir
from os.path import isfile, join
import argparse
import datetime
```
The functions within Import Data are as follows:
- two ways of searching through an array- binary and linear. both take a datetime value, find the associated value that corresponds within your time series, and returns the list of values associated with that key.
- roundTimeArray takes an object (from ImportData) and a resolution, whidch is the interval you want to round your times to (in minutes.) It returns an iterable zip object of time + value pairs. NOTE: if rounded times end up with repeats (esp as you increase resolution value, this may happen), the function will sum values if the values correspond to: activity, bolus, meal, adn will avg the values if they correspond to hr, cgm, smbg. If your csv file isn't one of these types, no duplication method is employed and you'll get a message saying so.
- printArray takes a list of zip objects, strings with column labels for the data value (annotation_list), the file name you want to print as (base_name), and the name from annotation list that you want to align data with (key_file). A csv is created for you.


***UPDATE as of December 3rd, 2019***
- *pandas_import.py* is a script that takes various csv files and cleans and merges them. The files are: activity, basal, bolus, cgm, hr, meal, and smbg data.
- NAs are removed, strings are removed, and then all of the files are merged using the cgm file as a baseline (e.g. if an index exists in one file but not in a cgm file, that row is not merged in. AKA a left join on the cgm file.)
- after the files are merged, time stamps are rounded to either 5 or 15 minutes and data is either summed or averaged to a final aggregate file for each respective breakdown.
- the final merged data files are: *grouped_by_fifteen.csv* & *grouped_by_five.csv*

***Benchmarking Results ***
- reporting the time it took for pandas_import.py:
! [] (https://github.com/cu-swe4s-fall-2019/time-series-basics-ellenwaddle/blob/master/Benchmarking_pandas.png)
