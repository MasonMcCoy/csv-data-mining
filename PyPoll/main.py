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