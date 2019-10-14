import csv
import dateutil.parser
from os import listdir
from os.path import isfile, join
import argparse
import datetime


class ImportData:

    def __init__(self, data_csv):
        self._time = []
        self._value = []
        self._roundtime = []
        self._roundtimeStr = []

        # open file, create reader from csv.DictReader, read input times + vals
        with open(data_csv, 'r') as fhandle:
            reader = csv.DictReader(fhandle)
            for row in reader:
                if row['time'] = 'low':
                    row['time'] = 40
                    print('replacing low string found in file with 40')

                else:
                    if row['time'] = 'high':
                        row['time'] = 300
                        print('replacing high string found in file with 300')
                try:
                    self._time.append(dateutil.parser.parse(row['time']))

                except ValueError:
                    print('Bad input format for time')
                    print(row['time'])
                self._value.append(row['value'])
            fhandle.close()

        self.roundTime(5)

    def linear_search_value(self, key_time):
        for i in range(len(self._roundtimeStr)):
            curr = self._roundtimeStr[i]
            if key_time == curr:  #return list of vals associated with key_time
                return self._value[i]
            else:
                print('invalid time')
        return -1

    def binary_search_value(self,key_time): # optional extra credit
        lo = -1
        hi = len(self._roundtimeStr)
        while (hi - lo > 1):
            mid = (hi + lo) // 2

            if key_time == self._roundtimeStr[mid][0]:
                return self._roundtimeStr[mid][1]

            if (key_time < self._roundtimeStr[mid][0]):
                hi = mid
            else:
                lo = mid
        return -1
        # if none, return -1 and error message


def roundTimeArray(obj, res):
    # Inputs: obj (ImportData Object) and res (rounding resoultion)
    # objective:
    # create a list of datetime entries and associated values
    # with the times rounded to the nearest rounding resolution (res)
    # ensure no duplicated times
    # handle duplicated values for a single timestamp based on instructions in
    # the assignment
    # return: iterable zip object of the two lists
    # note: you can create additional variables to help with this task
    # which are not returned


def printArray(data_list, annotation_list, base_name, key_file):
    # combine and print on the key_file

if __name__ == '__main__':

    #adding arguments
    parser = argparse.ArgumentParser(description= 'A class to import, combine, and print data from a folder.',
    prog= 'dataImport')

    parser.add_argument('folder_name', type = str, help = 'Name of the folder')

    parser.add_argument('output_file', type=str, help = 'Name of Output file')

    parser.add_argument('sort_key', type = str, help = 'File to sort on')

    parser.add_argument('--number_of_files', type = int,
    help = "Number of Files", required = False)

    args = parser.parse_args()


    #pull all the folders in the file
    files_lst = # list the folders


    #import all the files into a list of ImportData objects (in a loop!)
    data_lst = []

    #create two new lists of zip objects
    # do this in a loop, where you loop through the data_lst
    data_5 = [] # a list with time rounded to 5min
    data_15 = [] # a list with time rounded to 15min

    #print to a csv file
    printLargeArray(data_5,files_lst,args.output_file+'_5',args.sort_key)
    printLargeArray(data_15, files_lst,args.output_file+'_15',args.sort_key)
