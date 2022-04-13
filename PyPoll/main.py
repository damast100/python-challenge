import os
import csv

path = "C:\\Users\\Derek\\Desktop\\"
election_csv = os.path.join(path, 'python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

# create lists to retain the information
votes = []
name_charles = []
name_diana = []
name_raymon = []

# open and read the CSV file
with open(election_csv, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	
	# skip the header
	header = next(csvreader)

	# iterate through each row in the CSV file
	for row in csvreader:

		# add the number of lines to the list to get the sum at a later point
		votes.append(int(row[0]))

		#looking to see if these names appear and adding them to the lists to get the sum at a later point
		if row[2] == "Charles Casper Stockham":
			name_charles.append(row[2])
		elif row[2] == "Diana DeGette":
			name_diana.append(row[2])
		elif row[2] == "Raymon Anthony Doane":
			name_raymon.append(row[2])

# creating variables with calculations to make the print statements easier
total_votes = len(votes)
charles_votes = len(name_charles)
diana_votes = len(name_diana)
raymon_votes = len(name_raymon)
charles_percentage = round(((charles_votes / total_votes) * 100), 3)
diana_percentage = round(((diana_votes / total_votes) * 100), 3)
raymon_percentage = round(((raymon_votes / total_votes) * 100), 3)

# print statements
print("Election Results")
print("----------------------")
print(f'Total Votes: {total_votes}')
print(f'Charles Casper Stockham: {charles_percentage}% ({charles_votes})')
print(f'Diana DeGette: {diana_percentage}% ({diana_votes})')
print(f'Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})')
print("---------------------")
print(f'Winner : Diana DeGette')
print("----------------------")

# writing the information to the new file
output_file = os.path.join(path, 'python-challenge', 'PyPoll', 'Analysis', 'financial_analysis_election.txt')
with open (output_file, "w") as file:
	file.write("Election Results")
	file.write("\n")
	file.write("----------------------")
	file.write("\n")
	file.write(f'Total Votes: {total_votes}')
	file.write("\n")
	file.write(f'Charles Casper Stockham: {charles_percentage}% ({charles_votes})')
	file.write("\n")
	file.write(f'Diana DeGette: {diana_percentage}% ({diana_votes})')
	file.write("\n")
	file.write(f'Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})')
	file.write("\n")
	file.write("---------------------")
	file.write("\n")
	file.write(f'Winner : Diana DeGette')
	file.write("\n")
	file.write("----------------------")
