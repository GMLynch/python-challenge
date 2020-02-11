import os
import csv

#Path the csv file
csvpath = os.path.join('budget_data.csv')

#set the begining value
date = []
profit_losses = []
sumofb = 0
total_Avg_change = 0
last_num =0
change_average = {}
months = []



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
        # monthly change
        change_average[row[0]] = int(row[1]) - last_num
        last_num = int(row[1])

#create calculation variables
total_months = len(date)
greatest_increase = profit_losses[0]
greatest_decrease = profit_losses[0]
greatest_increase_month = date[0]
greatest_decrease_month = date[0]
profit_losses = 0



#Calculate the average change

for key, value in change_average.items():
    if key == date[0]:
        num = 0
    else:
        total_Avg_change = total_Avg_change + value
    

  #For loop to go through to find the greatest inc/dec and allocated month  
greatest_increase = max(zip(change_average.values(), change_average.keys()))
greatest_decrease = min(zip(change_average.values(), change_average.keys()))
greatest_decrease_month = (greatest_decrease[1] + "($" + str(int(greatest_decrease[0]))+")")
greatest_increase_month = (greatest_increase[1] + "($" + str(int(greatest_increase[0]))+")")

#Summary
print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: ${sumofb}")
print(f"Average Change: ${total_Avg_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month}")
print(f"Greatest Decrease in Profits: {greatest_decrease_month}")



#create a text find capturing the results
new_file = open("PyBank_Results.txt", "w")
new_file.write("Financial Analysis /n")
new_file.write(f"Total Months: {total_months} /n")
new_file.write(f"Total: ${sumofb} /n")
new_file.write(f"Average Change: ${total_Avg_change} /n")
new_file.write(f"Greatest Increase in Profits: {greatest_increase_month} + (${greatest_increase}) /n")
new_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} + (${greatest_decrease}) /n")   
    



    




