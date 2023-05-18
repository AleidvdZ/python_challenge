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

#set empty list to dump csv columns into
ballot_id = []
county = []
candcolumn = []

#recipient lists
candidate_list = []
total_vote_list = []
combo_list = []

#variables


with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)

    #dump all of the csv columns into list
    for row in csv_reader:
        ballot_id.append(row[0])
        county.append(row[1])
        candcolumn.append(row[2])

#put unique candidate names in list
candidate_list = set(candcolumn)

#calculate number of votes based on ballot number
no_votes = len(ballot_id)

candidate = ""
name = ""
cand_vote = 0

for candidate in candidate_list:
    for name in candcolumn:
        if name == candidate:
            cand_vote = cand_vote + 1
     
    
    total_vote_list.append(cand_vote)  
    combo_list.extend([candidate, cand_vote])
    cand_vote = 0

# Need to calculate %
#for item in combo_list:
#    print(item)
  
def convert(combo_list);
    
    

# Need to print the candidates in order alphabetical by first name followed by % and number in parenthesis


print (no_votes)
print (candidate_list)
print (total_vote_list)
print (combo_list)

#print output
print ()
print ("Election Results")
print ()
print ("----------------------------")
print ()
print (f"Total Votes: {no_votes}")
print ()
print ("----------------------------")
print ()
