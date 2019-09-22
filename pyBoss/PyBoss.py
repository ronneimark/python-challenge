# This is main.py in pyBank

# Load csv file
import os
import csv
import sys

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

csvpath = os.path.join('employee_data.csv')

sys.stdout = open('clean_employee_data.csv', 'w+')

print("EmpID, LastName, FirstName, DOB, SSN, State")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    for row in csvreader:

        namesplit = row[1].split(" ", 1)
        first_name = namesplit[0]
        last_name = namesplit[1]
        
        last_4_ss = row[3][-4:]

        st = us_state_abbrev[row[4]]
        
        print(f"{row[0]}, {last_name}, {first_name}, {row[2]}, ***-**-{last_4_ss}, {st}")











# The Name column should be split into separate First Name and Last Name columns.


# The DOB data should be re-written into MM/DD/YYYY format.


# The SSN data should be re-written such that the first five numbers are hidden from view.


# The State data should be re-written as simple two-letter abbreviations.




# Special Hint: You may find this link to be helpful—Python Dictionary for State Abbreviations.