import os
import csv

path = "C:\\Users\\Derek\\Desktop\\"
budget_csv = os.path.join(path, 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

total_months = []
total_revenue = []
profit_change = []

#Count the total months
with open(budget_csv, 'r') as csvfile:
	next(csvfile)
	csvreader = csv.reader(csvfile, delimiter=",")
	data = list(csvreader)
	row_count = len(data)
	print(f'Total Months: {row_count}')
	
total = 0

with open(budget_csv, 'r') as csvfile:
	next(csvfile)
	csvreader = csv.reader(csvfile, delimiter=",")
	for row in csvreader:
		total = total + int(row[1])
	print(f'Total: ${total}')