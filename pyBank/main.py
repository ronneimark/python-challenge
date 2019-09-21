# This is main.py in pyBank

# Load csv file
import os
import csv
import sys

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    
    # Set totals to 0 before reading each row's data to store 
    months = 0
    total = 0
    greatest_increase = 0
    greatest_decrease = 0
    
    for row in csvreader:

        months += 1
        total += float(row[1])

        if float(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        if float(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]


# Print out once to the terminal and once to file "PyBank.txt"

for i in range(2):

    print("")

    print("Financial Analysis")

    print("")

    print("------------------------------------------")

    print("")

    # The total number of months included in the dataset
    print(f"Total months: {months}")

    # The net total amount of "Profit/Losses" over the entire period
    print(f"Total: ${int(total)}")

    # The average of the changes in "Profit/Losses" over the entire period
    average_change = round(total/months, 2)

    print(f"Average Change: ${average_change}")

    # The greatest increase in profits (date and amount) over the entire period
    print(f"Greatest increase in profits: {greatest_increase_month} (${greatest_increase})")

    # The greatest decrease in losses (date and amount) over the entire period
    print(f"Greatest decrease in profits: {greatest_decrease_month} (${greatest_decrease})")

    sys.stdout = open('PyBank.txt', 'w+')