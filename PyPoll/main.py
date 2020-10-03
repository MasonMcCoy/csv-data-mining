# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:11:38 2020

@author: Mason
"""

'Script for PyPoll Python Challenge'

import csv

with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyPoll/Resources/03-Python_HW_Instructions_PyPoll_Resources_election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    row_count = sum(1 for row in csvreader)
    row_count = row_count - 1
    print(row_count)
    #returns 3521001?
    candidates = []
    for column in csvreader:
        for row in column:
            if column.header == 'Candidate' and row not in candidates:
                    candidates.append(row)
    print(candidates)
    
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
print:('Election Results')
print:('-------------------------')
print:('Total Votes: ')
print:('-------------------------')
print:('Khan: ')
print:('Correy: ')
print:('Li: ')
print:("O'Tooley: ")
print:('-------------------------')
print:('Winner: ')
print:('-------------------------')

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