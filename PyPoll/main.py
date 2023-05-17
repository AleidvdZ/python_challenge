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

#variables
start_vote = 1
cand_vote = 0


with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)

    # count the number of lines in the csv after the header (already accounted for)
    #no_votes = len(list(csv_reader))
 
    #dump all of the csv columns into list
    for row in csv_reader:

        ballot_id.append(row[0])
        county.append(row[1])
        candcolumn.append(row[2])

#put unique candidate names in list
candidate_list = set(candcolumn)

#calculate number of votes based on ballot number
no_votes = len(ballot_id)

#count numbere of votes for each candidate
#set empty candidate variable
candidate = ""

for name in range(0, len(candcolumn)):
    for cand in range(0, len(candidate_list)):
        if str(name) == str(candidate[cand]):
            cand_vote=cand_vote + 1
            total_vote_list.append(cand_vote)   
#need to think this through

        

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


print (no_votes)
print (candidate_list)
print (total_vote_list)
