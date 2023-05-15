#Your task is to create a Python script that analyzes the records to calculate 
#each of the following values:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in profits (date and amount) over the entire period

#Output
    #Financial Analysis
    #----------------------------
    #Total Months: 86
    #Total: $22564198
    #Average Change: $-8311.11
    #Greatest Increase in Profits: Aug-16 ($1862002)
    #Greatest Decrease in Profits: Feb-14 ($-1825558)

#First couple of lines in the csv
    #Date,Profit/Losses
    #Jan-10,1088983

#read the csv file
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# Lists to store data and variables
date = []
profit_loss = []
pl_changelist = []
total_pl = 0
pl_change = 0
maxmo = ""
minmo = ""
changesum = []
changeave = 0.00

with open(csvpath) as  csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)

    for row in csv_reader:

        # Add date
        date.append(row[0])

        # Add population
        profit_loss.append(row[1])

    # Add up the total profit/loss
    # Iterate each element in list
    # and add them in variable total
for ele in range(0, len(profit_loss)):
    total_pl = int(total_pl) + int(profit_loss[ele])

#total number of months in dataset
total_months = (len(date))

#changes in profit/loss over the entire period 
x=1
for ele in range (0, len(profit_loss)):
    if x <= (len(profit_loss)-1):
        secondno = (profit_loss[x])
        firstno = (profit_loss[x-1])
        pl_change = int(secondno) - int(firstno)
        pl_changelist.append(pl_change)
        pl_change = 0
        x +=1

#determining max/min change and month
max_pl = 0
min_pl = 0
for i in range (0, len(pl_changelist)):
    if pl_changelist[i] > max_pl:
            max_pl = pl_changelist[i]
            #maxmo = date.index[i]

    elif pl_changelist[i] < min_pl:
            min_pl = pl_changelist[i]
            #minmo = date.index(y)

# the average over those changes
#changeave = float(changesum/total_months)

print (total_months)
print (total_pl)
print (changeave)
print (max_pl)
#print (maxmo)
print (min_pl)
#print (minmo)
print (pl_changelist)
print (date)