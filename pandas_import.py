import numpy as np
import pandas as pd
import datetime as dt
'''
this script cleans, merges, then aggregates the '_small.csv' data frames. it
will either sum or avg values across 5 or 15 min intervals. output is
called 'grouped_by ... .csv'
'''

#import csv files in the smallData folder to pandas df objects
activity = pd.read_csv('activity_small.csv')
basal = pd.read_csv('basal_small.csv')
bolus = pd.read_csv('bolus_small.csv')
cgm = pd.read_csv('cgm_small.csv')
hr = pd.read_csv('hr_small.csv')
meal = pd.read_csv('meal_small.csv')
smbg = pd.read_csv('smbg_small.csv')

# If pandas imported some "junk" that we had in the spreadsheet and
# resulted in extra "Unnamed" columns, we can filter for and drop them by using
# text parsing (str.contains())
activity = activity.loc[:, ~activity.columns.str.contains('^Unnamed')]
basal = basal.loc[:, ~basal.columns.str.contains('^Unnamed')]
bolus = bolus.loc[:, ~bolus.columns.str.contains('^Unnamed')]
cgm = cgm.loc[:, ~cgm.columns.str.contains('^Unnamed')]
smbg = cgm.loc[:, ~smbg.columns.str.contains('^Unnamed')]
hr = hr.loc[:, ~hr.columns.str.contains('^Unnamed')]
meal = meal.loc[:, ~meal.columns.str.contains('^Unnamed')]

#lets rename columns
activity.rename(columns={"value":"activity"},inplace=True)
basal.rename(columns={"value":"basal"},inplace=True)
bolus.rename(columns={"value":"bolus"},inplace=True)
cgm.rename(columns={"value":"cgm"},inplace=True)
smbg.rename(columns={"value":"smbg"},inplace=True)
hr.rename(columns={"value":"hr"},inplace=True)
meal.rename(columns={"value":"meal"},inplace=True)


#change to date time objects
activity.time = pd.to_datetime(activity.time)
basal.time = pd.to_datetime(basal.time)
bolus.time = pd.to_datetime(bolus.time)
cgm.time = pd.to_datetime(cgm.time)
smbg.time = pd.to_datetime(smbg.time)
hr.time = pd.to_datetime(hr.time)
meal.time = pd.to_datetime(meal.time)


#set indices
activity.set_index('time',inplace=True)
basal.set_index('time',inplace=True)
bolus.set_index('time',inplace=True)
cgm.set_index('time',inplace=True)
smbg.set_index('time',inplace=True)
hr.set_index('time',inplace=True)
meal.set_index('time',inplace=True)


#for activity, remove strings. all else, change value to ints
activity.activity=activity.activity.astype(str)
uniq = activity.activity[~activity.activity.str.isnumeric()].unique()
activity.activity.replace('###', 0, inplace= True)
activity.activity.replace('0+C4218', 0, inplace= True)
activity.activity.replace('nan', 0, inplace= True)


activity.activity=activity.activity.astype(int)
basal.basal=basal.basal.astype(int)
bolus.bolus=bolus.bolus.astype(int)
cgm.cgm=cgm.cgm.astype(int)
smbg.smbg=smbg.smbg.astype(int)
hr.hr=hr.hr.astype(int)
meal.meal=meal.meal.astype(int)

#merge all dfs based off cgm idx - left join
joinFrame = cgm.join([hr, meal, basal, bolus, smbg, activity], how='left')

#lets fill in any nan values with 0. We will do this inplace
joinFrame.fillna(0,inplace=True)

#create columns w rounded values
five_df = joinFrame.index.round('5min')
fifteen_df = joinFrame.index.round('15min')
joinFrame.insert(len(joinFrame.columns),"five",five_df)
joinFrame.insert(len(joinFrame.columns),"fifteen",fifteen_df)

#remove unwanted columns
joinFrame.drop(columns=['Id_x'], inplace = True)
joinFrame.drop(columns=['Id_y'], inplace = True)
joinFrame.drop(columns=['patient_x'], inplace = True)
joinFrame.drop(columns=[' With meal'], inplace = True)
joinFrame.drop(columns=['patient_y'], inplace = True)
joinFrame.drop(columns=['patient_x'], inplace = True)
joinFrame.drop(columns=['id'], inplace = True)


#group by
# sum: activity, bolus, meal
# avg: smbg, hr, cgm, basal
five_sum = joinFrame.groupby('five')[['activity', 'bolus', 'meal']]
fifteen_sum = joinFrame.groupby('fifteen')[['activity', 'bolus', 'meal']]

five_avg = joinFrame.groupby('five')[['smbg', 'hr', 'cgm', 'basal']]
fifteen_avg = joinFrame.groupby('fifteen')[['smbg', 'hr', 'cgm', 'basal']]

#merge two dfs and then write to CSV files
fives = five_sum.join([five_avg], how = 'outer')
fifteens = five_sum.join([fifteen_avg], how = 'outer')

fives.to_csv('grouped_by_five.csv', index = True , header = True )
fifteens.to_csv('grouped_by_fifteen.csv', index = True , header = True )
