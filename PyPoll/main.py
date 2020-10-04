# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:11:38 2020

@author: Mason
"""

'Script for PyPoll Python Challenge'

import csv
candidates = []
khan_voters = []
correy_voters = []
li_voters = []
otooley_voters = []
    
#calculates total number of votes cast for all candidates
with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyPoll/Resources/03-Python_HW_Instructions_PyPoll_Resources_election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    total_votes = sum(1 for row in csvreader)
    
#stores candidate names in a list and caluclates total number of votes cast for each candidate
with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyPoll/Resources/03-Python_HW_Instructions_PyPoll_Resources_election_data.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ',')   
    
    for row in csvreader:
        candidate = row['Candidate']
        if candidate not in candidates:
            candidates.append(candidate)     
        khan_voters.append(candidate.count('Khan'))
        correy_voters.append(candidate.count('Correy'))
        li_voters.append(candidate.count('Li'))
        otooley_voters.append(candidate.count("O'Tooley"))
    
    khan_votes = sum(khan_voters)
    correy_votes = sum(correy_voters)
    li_votes = sum(li_voters)
    otooley_votes = sum(otooley_voters)
   
    #calculates the percentage of the popular vote each candidate recieved
    khan_percent = round((khan_votes / total_votes) * 100, 3)
    correy_percent = round((correy_votes/total_votes) * 100, 3)
    li_percent = round((li_votes/total_votes) * 100, 3)
    otooley_percent = round((otooley_votes/total_votes) * 100, 3)
     
    #determines winner of the election based on popular vote
    vote_winner = ''
    if khan_percent > correy_percent and li_percent and otooley_percent:
        vote_winner = 'Khan'
    elif correy_percent > li_percent and otooley_percent:
        vote_winner = 'Correy'
    elif li_percent > otooley_percent:
        vote_winner = 'Li'
    else:
        vote_winner = "O'Tooley"
   
    #prints analytic info to terminal
print('Election Results')
print('-------------------------')
print('Total Votes: ', total_votes)
print('-------------------------')
print(candidates[0], ":", khan_percent, "% (", khan_votes, ")")
print(candidates[1], ":", correy_percent, "% (", correy_votes, ")")
print(candidates[2], ":", li_percent, "% (", li_votes, ")")
print(candidates[3], ":", otooley_percent, "% (", otooley_votes, ")")
print('-------------------------')
print('Winner: ', vote_winner)
print('-------------------------')

#Generates .txt file "poll_results" with voting info
txt = open('poll_results.txt', 'w')
txt.write('Election Results\n')
txt.write('----------------------------\n')
txt.write('Total Votes: ' + str(total_votes) + "\n")
txt.write('-------------------------\n')
txt.write(candidates[0] + ": " + str(khan_percent) + "% (" + str(khan_votes) + ")\n")
txt.write(candidates[1] + ": " + str(correy_percent) + "% (" + str(correy_votes) + ")\n")
txt.write(candidates[2] + ": " + str(li_percent) + "% (" + str(li_votes) + ")\n")
txt.write(candidates[3] + ": " + str(otooley_percent) + "% (" + str(otooley_votes) + ")\n")
txt.write('-------------------------\n')
txt.write('Winner: ' + vote_winner + '\n')
txt.write('-------------------------')
txt.close()