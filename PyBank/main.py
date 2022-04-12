import os
import csv

path = "C:\\Users\\Derek\\Desktop\\"
budget_csv = os.path.join(path, 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

total_months = []
total_revenue = []

#Count the total months and revenue
with open(budget_csv, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader)
	for row in csvreader:
		total_months.append(row[0])
		total_revenue.append(int(row[1]))

print("Financial Analysis")
print("------------------------")
print(f'Total Months: {len(total_months)}')
print(f'Total: ${sum(total_revenue)}')

net_change_list = []
date_change_list = []
with open(budget_csv, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	header = next(csvreader)
	first_row = next(csvreader)
	prev_net = int(first_row[1])
	for row in csvreader:
		net_change = int(row[1]) - prev_net
		prev_net = int(row[1])
		net_change_list.append(net_change)
		date_change_list.append(row[0])
	net_average = round((sum(net_change_list) / len(net_change_list)), 2)

increase = max(net_change_list)
decrease = min(net_change_list)
increase_index = net_change_list.index(max(net_change_list))
decrease_index = net_change_list.index(min(net_change_list))
month_increase = date_change_list[increase_index]
month_decrease = date_change_list[decrease_index]

print(f'Average Change: ${net_average}')
print(f'Greatest Increase in Profits: {month_increase} (${increase})')
print(f'Greatest Decrease in Profits: {month_decrease} (${decrease})')

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
	