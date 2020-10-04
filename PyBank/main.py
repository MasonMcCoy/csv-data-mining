# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:09:48 2020

@author: Mason
"""

'Script for PyBank Python Challenge'

import csv
import os.path

#calculates the number of months in the dataset
with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv', 'r') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    total_months = sum(1 for row in csvreader)
    
#calculates the sum of all charges
with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv', 'r') as csvfile:    
    csvreader = csv.reader(csvfile)
    net_charges = 0
    next(csvreader)
    for row in csvreader:
        net_charges = net_charges + int(row[1])
                      
#calculates average change of all charges
average_charge = net_charges/total_months
average_change = average_charge/total_months

#Finds month and value of greatest increase/decrease
with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv', 'r') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    reader = list(csvreader)
    decrease_date = ''
    increase_date = ''
    local_max = 0
    global_max = 0
    local_min = 0
    global_min = 0
    greatest_decrease = 0
    greatest_increase = 0
    decrease_date = 0
    increase_date = 0
    previous = reader[0]
    for idx, row in enumerate(reader):
        profit = row[1]
        local_max = max(local_max, int(profit) - int(previous[1]))
        global_max = max(global_max, local_max)
        local_min = min(local_min, int(profit) - int(previous[1]))
        global_min = min(global_min, local_min)
        previous = row
        if greatest_decrease > int(profit):
            decrease_date = row[0]
            greatest_decrease = global_min
        if greatest_increase < int(profit):
            increase_date = row[0]
            greatest_increase = global_max
    print(global_max, global_min)
    print(decrease_date, increase_date)
    
    #column? csvread vs. reader?

#prints analytic info to terminal
print('Financial Analysis')
print('----------------------------')
print('Total Months:', total_months)
print('Total:', net_charges)
print('Average Change: ', average_change)
print('Greatest Increase in Profits:', increase_date, '(', greatest_increase, ')')
print('Greatest Decrease in Profits:', decrease_date,'(', greatest_decrease, ')')

#Generates .txt file "results" with analyic info
txt = open(os.path.join('Analysis', 'bank_results.txt'), 'w')
txt.write("Financial Analysis")
txt.write('----------------------------\n')
txt.write('Total Months: ' + str(total_months) + '\n')
txt.write('Total: ' + str(net_charges) + '\n')
txt.write('Average Change: ' + str(average_change) + '\n')
txt.write('Greatest Increase in Profits: ' + str(increase_date) + ' (' + str(greatest_increase) + ')\n')
txt.write('Greatest Decrease in Profits: ' + str(decrease_date) + ' (' + str(greatest_decrease) + ')')
txt.close()
    
