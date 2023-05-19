#read the csv file
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#Set empty list to dump csv columns into
ballot_id = []
county = []
candcolumn = []

#Set recipient empty lists
candidate_list = []
total_vote_list = []
combo_list = []

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

#Print header and total votes
print ()
print ("Election Results")
print ()
print ("----------------------------")
print ()
print (f"Total Votes: {no_votes}")
print ()
print ("----------------------------")

#set variables for serching through all of the votes relative to the candidates in the summary list
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

# Set variables to count per candidate and to calculate percent of total for each candidate
item = 0
cand_name = ""
cand_count = 0
cand_percent = 0
count_comp = 0
cand_comp = ""

#Set empty list for print
cand_print_ls = []

for x in range(0,(len(combo_list)-1)):
    if (x % 2) == 0:
        curr = combo_list[x]
        nextv = combo_list[x+1]
        cand_name = curr
   
        cand_count = nextv
        
        cand_percent = int(cand_count)/no_votes*100
        cand_percent_r = round (cand_percent, 3)

        #Print candidate stats
        print ()
        print (f"{cand_name}: {cand_percent_r}% ({cand_count})")
        
        #Math to determine winner
        if cand_count > count_comp:
           count_comp = cand_count
           cand_comp = cand_name

print ()
print ("----------------------------")
print ()
print (f"Winner: {cand_comp}")
print ()
print ("----------------------------")


#printing to .txt file
import sys
stdoutOrigin=sys.stdout
sys.stdout = open("PyPoll_AvdZ.txt","w")

#Print header and total votes
print ()
print ("Election Results")
print ()
print ("----------------------------")
print ()
print (f"Total Votes: {no_votes}")
print ()
print ("----------------------------")

#set variables for serching through all of the votes relative to the candidates in the summary list
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

# Set variables to count per candidate and to calculate percent of total for each candidate
item = 0
cand_name = ""
cand_count = 0
cand_percent = 0
count_comp = 0
cand_comp = ""

#Set empty list for print
cand_print_ls = []

for x in range(0,(len(combo_list)-1)):
    if (x % 2) == 0:
        curr = combo_list[x]
        nextv = combo_list[x+1]
        cand_name = curr
   
        cand_count = nextv
        
        cand_percent = int(cand_count)/no_votes*100
        cand_percent_r = round (cand_percent, 3)

        #Print candidate stats
        print ()
        print (f"{cand_name}: {cand_percent_r}% ({cand_count})")
        
    #Math to determine winner
    if cand_count > count_comp:
        count_comp = cand_count
        cand_comp = cand_name

print ()
print ("----------------------------")
print ()
print (f"Winner: {cand_comp}")
print ()
print ("----------------------------")

sys.stdout.close()
sys.stdout=stdoutOrigin

