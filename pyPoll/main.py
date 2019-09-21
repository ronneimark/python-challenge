# This is main.py in PyPoll

# Open Data file
# Load csv file
import os
import csv
import sys

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    voterID, county, candidates = [], [], {}

    votes_cast = 0

    for row in csvreader:

        # Create list of candidates in datafile

        if row[2] not in candidates:

            candidates.update({row[2]:1})

        elif row[2] in candidates:

            candidates[row[2]] += 1 

        votes_cast += 1

# Print out once to the terminal and once to file "PyBank.txt"

for i in range(2):

    print("")
    print("Election Results")
    print("")
    print("----------------------------")
    print("")

    # The total number of votes cast

    print(f"Total Votes: {votes_cast}")
    print("")
    print("----------------------------")
    print("")

    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won

    winner_votes = 0

    for person in candidates:

        percent = round(candidates[person]/votes_cast*100, 3)
    
        print(f"{person}   {percent}%   ({candidates[person]})")

        if candidates[person] > winner_votes:

            winner_votes = candidates[person]
        
            winner = person

    # The winner of the election based on popular vote.

    print("")
    print("----------------------------")
    print("")

    print(f"Winner: {winner}")

    print("")
    print("----------------------------")

    sys.stdout = open('PyPoll.txt', 'w+')