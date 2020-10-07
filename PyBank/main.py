#import
import os
import csv

#make path
csvpath=os.path.join('..', 'Resources','budget-data.csv')
#open file
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

#initialize accumulators
number_of_months=0
profit_loss=0

for row in csvreader:
    #find total number of months
    number_of_months+=1
    #add each row up to see total
    profit_loss=row[1]+profit_loss
print(number_of_months)
print(profit_loss)


