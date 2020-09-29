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
    print(total_months)
    
#calculates the sum of all charges
with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv', 'r') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')   
    net_charges = 0
    for row in csvreader:
        for column in row:
            if column == 'Profit/Losses':
                #net_charges += int(column)
    #net_charges = sum(int(row[1])) for row in csvreader
                print(net_charges)       
                
#calculates average change of all charges
#average_change = net_charges/row_count

#finds the greatest increase in profits
with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv', 'r') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')      
    next(csvreader)
    greatest_increase = max(int(column[1].replace(',', '')) for column in csvreader)
    print(greatest_increase)
    #if row == greatest_increase:
        #greatest_month = int(row in column[1])
        #print(greatest_month)
        
#finds the greatest decrease in losses
with open('C:/Users/Mason/Data_Bootcamp/Python_Challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv', 'r') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')      
    next(csvreader)
    greatest_loss = min(int(column[1].replace(',', '')) for column in csvreader)
    print(greatest_loss)

#prints analytic info to terminal
print:('Financial Analysis')
print:('----------------------------')
print:('Total Months: ' + total_months)
print:('Total: ' + net_charges)
print:('Average Change: ')
print:('Greatest Increase in Profits: ')
print:('Greatest Decrease in Profits: ' )

#Generates .txt file "results" with analyic info
txt = open('bank_results.txt', 'wb')
txt.write('Financial Analysis\n'.encode())
txt.write('----------------------------\n'.encode())
txt.write('Total Months: \n'.encode())
txt.write('Total: \n'.encode())
txt.write('Average Change: \n'.encode())
txt.write('Greatest Increase in Profits: \n'.encode())
txt.write('Greatest Decrease in Profits: '.encode())
txt.close()
    
#How to print to correct folder?