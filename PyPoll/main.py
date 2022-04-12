import os
import csv

path = "C:\\Users\\Derek\\Desktop\\"
election_csv = os.path.join(path, 'python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

votes = []
name_charles = []
name_diana = []
name_raymon = []
with open(election_csv, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	header = next(csvreader)
	for row in csvreader:
		votes.append(int(row[0]))
		if row[2] == "Charles Casper Stockham":
			name_charles.append(row[2])
		elif row[2] == "Diana DeGette":
			name_diana.append(row[2])
		elif row[2] == "Raymon Anthony Doane":
			name_raymon.append(row[2])

total_votes = len(votes)
charles_votes = len(name_charles)
diana_votes = len(name_diana)
raymon_votes = len(name_raymon)
charles_percentage = round(((charles_votes / total_votes) * 100), 3)
diana_percentage = round(((diana_votes / total_votes) * 100), 3)
raymon_percentage = round(((raymon_votes / total_votes) * 100), 3)

print(total_votes)
print(f'Percentage: {charles_percentage}%')
print(diana_percentage)
print(raymon_percentage)