#import
import os
import csv
#import codecs

#make path
csvpath='/Users/kimkockenmeister/Desktop/hw3/python_HW3/PyBank/Resources/budget_data.csv'

#open file
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    if csv.Sniffer().has_header:
        next(csvreader)
    #print("hi")
    #csvReader = csv.reader(codecs.open('budget_data.csv', 'rU', 'utf-16'))
    #header=next(csvreader)
    #data=[r for r in reader]

#initialize accumulators
    number_of_months=0
    totalrevenue=0
    average=0
    all_differences=[]
    greatest_increase=0
    greatest_decrease=0
    greatestmonth=0
    leastmonth=0
   
    
    for row in csvreader:
    #keep track of the starting values
        last_profit=int(row[1])
        max_increase=int(row[1])
        greatest_increase=int(row[1])
        greatest_decrease=row[0]
    #find The total number of months included in the dataset
        number_of_months+=1

    # The net total amount of "Profit/Losses" over the entire period
        totalrevenue=int(row[1])+totalrevenue

    #find changes
        #change is difference from this row to the last one
        change=int(row[1]) - last_profit
        #add it to the list of all changes
        all_differences.append(change)
        #reset the last profit for next time
        last_profit = int(row[1])

    #The greatest increase/decrease in profits (date and amount) over the entire period
         #find the dates too
        if int(row[1]) > greatest_increase:
            #if it is bigger you want it to now equal that value 
            greatestincrease=int(row[1])
            #Month associated with it is
            greatestmonth=int(row[0])
        if int(row[1]) > greatest_decrease:
            #if it is bigger you want it to now equal that value 
            greatest_decrease=int(row[1])
            #Month associated with it is
            leastmonth=int(row[0])

       
       
    #The average of the changes in "Profit/Losses" over the entire period
    average=sum(all_differences)/len(all_differences)
    max=max(all_differences)
    min=min(all_differences)

    #print all it out 
    print("Financial Analysis")  
    print("----------------------------")
    print("Total Months:" + str(number_of_months))      
    print("Total:" + str(totalrevenue))
    print("Average Change: " + str(average))
    print("Greatest Increase in Profits:" + greatestmonth + str(greatest_increase))
    print("Greatest Decrease in Profits:" + leastmonth + str(gratest_decrease))
