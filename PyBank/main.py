# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:09:48 2020

@author: Mason
"""

'Script for PyBank Python Challenge'

import csv

with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv', 'r') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')
    row_count = sum(1 for row in csvreader)
    row_count = row_count - 1
    print(row_count)
    
with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv', 'r') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')   
    net_charges = 0
    for row in csvreader:
        for column in row:
            if column == 'Profit/Losses':
                #net_charges += int(column)
    #net_charges = sum(int(row[1])) for row in csvreader
                print(net_charges)             
                
#net_charges/row_count
