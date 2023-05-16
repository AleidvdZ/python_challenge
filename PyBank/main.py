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
total_sum = 0

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
            maxmo = str(date[(i+1)])

    elif pl_changelist[i] < min_pl:
            min_pl = pl_changelist[i]
            minmo = str(date[(i+1)])

#the average over those changes
#changeave = int(pl_changelist/total_months)
for i in range (0,len(pl_changelist)):
    total_sum = pl_changelist[i] + total_sum

changeave = total_sum/(total_months-1)
changeave_rd = round(changeave,2)

#Output
    #Financial Analysis
    #----------------------------
    #Total Months: 86
    #Total: $22564198
    #Average Change: $-8311.11
    #Greatest Increase in Profits: Aug-16 ($1862002)
    #Greatest Decrease in Profits: Feb-14 ($-1825558)

#print output
print ()
print ("Financial Analysis")
print ()
print ("----------------------------")
print ()
print (f"Total Months: {total_months}")
print ()
print (f"Total: ${total_pl}")
print ()
print (f"Average Change: ${changeave_rd}")
print ()
print (f"Greatest Increase in Profits: {maxmo} (${max_pl})")
print ()
print (f"Greatest Decrease in Profits: {minmo} (${min_pl})")

#Print to .txt file
with open("PyBank_AvdZ.txt", "a") as f:
    print ("", file=f)
    print ("Financial Analysis", file=f)
    print ("", file=f)
    print ("----------------------------", file=f)
    print ("", file=f)
    print (f"Total Months: {total_months}", file=f)
    print ("", file=f)
    print (f"Total: ${total_pl}", file=f)
    print ("", file=f)
    print (f"Average Change: ${changeave_rd}", file=f)
    print ("", file=f)
    print (f"Greatest Increase in Profits: {maxmo} (${max_pl})", file=f)
    print ("", file=f)
    print (f"Greatest Decrease in Profits: {minmo} (${min_pl})", file=f)



