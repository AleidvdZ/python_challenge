#instructions - Output
    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote

#todo
#read the csv file
#total number of votes - count
#list of candidates
#numbere of votes per candidate
#percentage for each candidate
#winner based on highest percentage
#print "Election Results
#print "-------------------------"
#print "Total" and numbere of votes, use f string
#print "-------------------------"
#print each canditate: percent out to 3 decimal places (double) and total voltes in parenthesis f string
#print "-------------------------"
#print "Winner:" + candidate with highest number of votes

#This is what is in csv (first two rows)
#Ballot ID,County,Candidate
#1323913,Jefferson,Charles Casper Stockham

#read the csv file
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#set variables
candidate_list = []
total_vote_list = []
start_vote = 1
cand_vote = 0
start_candidate = ""

# Create a list to store data to sort
candcolumn = []
#dump all of the candidate names in here and then pick out the unique ones?

with open(csvpath) as  csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)

    # count the number of lines in the csv after the header (already accounted for)
    no_votes = len(list(csv_reader))
 
    # Create empty list
    indiv_cand = []

    #dump all of the candidate names in here and then pick out the unique ones?

    for row in csv_reader:
        # Create a list to store data to sort
        candcolumn = []
        # Add candidates
        candcolumn.append(row[2])

    # Create empty list
    indiv_cand = [] 
    for item in candcolumn:
        if item not in indiv_cand:
            indiv_cand.append(item)

    for item in indiv_cand:
        print (item)      

        # Read through each row of data after the header
    #for row in csv_reader:
    #    if row[2]==(start_candidate):
    #       cand_vote = start_vote + 1 
    #       candidate_list.append(str(row[2]))
         
    #    else:
    #       total_vote_list.append(cand_vote)
    #       start_candidate = "" 


         




#what I had morning of 5/14
    #    if str(row_number) != str(row_number-1):
    #        canditate= 
    #        candidate_list.append(str((row_number-1)[2]))
                    
    #start_candidate = str(candidate[2])


print(no_votes)
print(candidate_list)
print(total_vote_list)