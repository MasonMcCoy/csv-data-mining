# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:09:48 2020

@author: Mason
"""

'Script for PyBank Python Challenge'

import csv

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

#finds the greatest increase and greatest loss in profits
with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv', 'r') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')      
    next(csvreader)
    greatest_decrease = 0
    greatest_increase = 0
    decrease_date = 0
    increase_date = 0
    for idx, column in enumerate(csvreader):
        profit = column[1]
        if greatest_decrease > int(profit):
            decrease_date = column[0]
            greatest_decrease = int(profit)
        if greatest_increase < int(profit):
            increase_date = column[0]
            greatest_increase = int(profit)

#prints analytic info to terminal
print('Financial Analysis')
print('----------------------------')
print('Total Months: ', total_months)
print('Total: ', net_charges)
print('Average Change: ', average_change)
print('Greatest Increase in Profits: ', increase_date, '(', greatest_increase, ')')
print('Greatest Decrease in Profits: ', decrease_date,'(', greatest_decrease, ')')

#Generates .txt file "results" with analyic info
txt = open('bank_results.txt', 'w')
txt.write('Financial Analysis\n')
txt.write('----------------------------\n')
txt.write('Total Months: ' + str(total_months) + '\n')
txt.write('Total: ' + str(net_charges) + '\n')
txt.write('Average Change: ' + str(average_change) + '\n')
txt.write('Greatest Increase in Profits: ' + str(increase_date) + '(' + str(greatest_increase) + ')\n')
txt.write('Greatest Decrease in Profits: ' + str(decrease_date) + '(' + str(greatest_decrease) + ')')
txt.close()
    
#How to print to correct folder?