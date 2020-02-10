import os
import csv

#Path the csv file
csvpath = os.path.join('budget_data.csv')

#set the begining value
date = []
profit_losses = []
sumofb = 0


#define the function 
def print_budget_data(budget_data):
    date = str(budget_data[0])
    profit_losses = int(budget_data[1])

#Open and read the csv file
with open("budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Read the header
    csv_header = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        profit_losses.append(int(row[1]))
        sumofb = sumofb + int(row[1])

#create calculation variables
total_months = len(date)
greatest_increase = profit_losses[0]
greatest_decrease = profit_losses[0]
greatest_increase_month = date[0]
greatest_decrease_month = date[0]
profit_losses = 0


#For loop to go through to find the greatest inc/dec and allocated month
for i in range(profit_losses):
    if profit_losses[i] >= greatest_increase:
        greatest_increase = profit_losses[i]
        greatest_increase_month = date[i]
    elif profit_losses[i] <= greatest_decrease:
        greatest_decrease = profit_losses[i]
        greatest_decrease_month = date[i]
    
    

#Calculate the average change
average_change = round(sumofb/total_months, 2)
    
#Summary
print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: ${sumofb}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} + (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} + (${greatest_decrease})")

#Remove the # once results are accurate

#create a text find capturing the results
#new_file = open("PyBank_Results.txt", "w")
#new_file.write("Financial Analysis /n")
#new_file.write(f"Total Months: {total_months} /n")
#new_file.write(f"Total: ${sumofb} /n")
#new_file.write(f"Average Change: ${average_change} /n")
#new_file.write(f"Greatest Increase in Profits: {greatest_increase_month} + (${greatest_increase}) /n")
#new_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} + (${greatest_decrease}) /n")   
    



    




