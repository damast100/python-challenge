import os
import csv

path = "C:\\Users\\Derek\\Desktop\\"
budget_csv = os.path.join(path, 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

# create lists to retain the information
total_months = []
total_revenue = []

# open and read the CSV file
with open(budget_csv, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	# skip the header
	header = next(csvreader)

	# iterate through each row in the CSV file
	for row in csvreader:

	# add the number of lines to the lists to get the sum at a later point
		total_months.append(row[0])
		total_revenue.append(int(row[1]))

# print statements
print("Financial Analysis")
print("------------------------")
print(f'Total Months: {len(total_months)}')
print(f'Total: ${sum(total_revenue)}')


# create lists to retain the information
net_change_list = []
date_change_list = []

# open and read the CSV file a second time
with open(budget_csv, 'r') as csvfile:
	csvreader = csv.reader(csvfile)

	# skip the header
	header = next(csvreader)

	#skip the first row
	first_row = next(csvreader)
	prev_net = int(first_row[1])

	# iterate through each row in the CSV file to find the change in values over time
	for row in csvreader:
		net_change = int(row[1]) - prev_net
		prev_net = int(row[1])
		net_change_list.append(net_change)
		date_change_list.append(row[0])
	net_average = round((sum(net_change_list) / len(net_change_list)), 2)

# creating variables with calculations to make the print statements easier
increase = max(net_change_list)
decrease = min(net_change_list)
increase_index = net_change_list.index(max(net_change_list))
decrease_index = net_change_list.index(min(net_change_list))
month_increase = date_change_list[increase_index]
month_decrease = date_change_list[decrease_index]

# print statements
print(f'Average Change: ${net_average}')
print(f'Greatest Increase in Profits: {month_increase} (${increase})')
print(f'Greatest Decrease in Profits: {month_decrease} (${decrease})')

# writing the information to the new file
output_file = os.path.join(path, 'python-challenge', 'PyBank', 'Analysis', 'financial_analysis.txt')
with open(output_file, "w") as file:
	file.write("Financial Analysis")
	file.write("\n")
	file.write("-----------------------")
	file.write("\n")
	file.write(f'Total Months: {len(total_months)}')
	file.write("\n")
	file.write(f'Total: ${sum(total_revenue)}')
	file.write("\n")
	file.write(f'Average Change: ${net_average}')
	file.write("\n")
	file.write(f'Greatest Increase in Profits: {month_increase} (${increase})')
	file.write("\n")
	file.write(f'Greatest Decrease in Profits: {month_decrease} (${decrease})')
	