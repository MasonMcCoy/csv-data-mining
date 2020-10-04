# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:11:38 2020

@author: Mason
"""

'Script for PyPoll Python Challenge'

import csv
candidates = []

#calculates total number of votes cast for all candidates
with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyPoll/Resources/03-Python_HW_Instructions_PyPoll_Resources_election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    total_votes = sum(1 for row in csvreader)
    print(total_votes)
    


#stores candidate names in a list and caluclates total number of votes cast for each candidate
with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyPoll/Resources/03-Python_HW_Instructions_PyPoll_Resources_election_data1.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ',')   
    khan_voters = []
    correy_voters = []
    li_voters = []
    otooley_voters = []
    
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
    
    print(candidates)
    print(khan_votes)
    print(correy_votes)
    print(li_votes)
    print(otooley_votes)
    
    
   
        
    
    #(khan_votes/total_votes) * 100 = khan_percent
    #(correy_votes/total_votes) * 100 = correy_percent
    #(li_votes/total_votes) * 100 = li_percent
    #(otooley_votes/total_votes) * 100 = otooley_percent
    
    #vote_winner = ''
    #if khan_percent > correy_percent, li_percent, otooley_percent:
        #vote_winner = 'Khan'
    #elif correy_percent > li_percent, otooley_percent:
        #vote_winner = 'Correy'
    #elif li_percent > otooley_percent:
        #vote_winner = 'Li'
    #else:
        #vote_winner = "O'Tooley"
    
    #print:('Election Results')
    #print:(-------------------------)
    #print:('Total Votes: str(total_votes')
    #print:(-------------------------)
    #print:(candidate[1] + ": " + )
    #print:(candidate[2] + ": " + )
    #print:(candidate[3] + ": " + )
    #print:(-------------------------)
    #print:('Winner: ' + popular_winner)
    #print:(-------------------------)

    #prints analytic info to terminal
print('Election Results')
print('-------------------------')
print('Total Votes: ', total_votes)
print('-------------------------')
print(candidates[0])
print(candidates[1])
print(candidates[2])
print(candidates[3])
print('-------------------------')
print('Winner: ', vote_winner)
print('-------------------------')

#Generates .txt file "poll_results" with voting info
txt = open('poll_results.txt', 'wb')
txt.write('Election Results'.encode())
txt.write('----------------------------\n'.encode())
txt.write('Total Votes: \n'.encode())
txt.write('-------------------------\n'.encode())
txt.write('Khan: \n'.encode())
txt.write('Correy: \n'.encode())
txt.write('Li: \n'.encode())
txt.write("O'Tooley': \n".encode())
txt.write('-------------------------\n'.encode())
txt.write('Winner: \n'.encode())
txt.write('-------------------------'.encode())
txt.close()