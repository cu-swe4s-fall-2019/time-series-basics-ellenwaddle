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
-two ways of searching through an array- binary and linear. both take a datetime value, find the associated value that corresponds within your time series, and returns the list of values associated with that key.
-roundTimeArray takes an object (from ImportData) and a resolution, whidch is the interval you want to round your times to (in minutes.) It returns an iterable zip object of time + value pairs. NOTE: if rounded times end up with repeats (esp as you increase resolution value, this may happen), the function will sum values if the values correspond to: activity, bolus, meal, adn will avg the values if they correspond to hr, cgm, smbg. If your csv file isn't one of these types, no duplication method is employed and you'll get a message saying so.
-printArray takes a list of zip objects, strings with column labels for the data value (annotation_list), the file name you want to print as (base_name), and the name from annotation list that you want to align data with (key_file). A csv is created for you.
