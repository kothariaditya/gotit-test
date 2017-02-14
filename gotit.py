#!/usr/bin/python
import datetime
import json
import matplotlib.pyplot as plt
daily = {}
monthly = {}
december = {}
nye = {}
for i in range(1,13):
	for j in range(0,24):
		monthly.update({(i,j):0})
with open("problem_times.json") as input_file:
	data = json.load(input_file)
for mylist in data.values():
	for mydate in mylist:
		mystamp = datetime.datetime.strptime(mydate, '%Y-%m-%d %H:%M:%S')
		hour = mystamp.hour
		month = mystamp.month
		day = mystamp.day
		if hour in daily:
			daily[hour] = daily[hour] + 1
		else:
			daily[hour] = 1
		monthly[(month,hour)] = monthly[(month,hour)] + 1
		if day in december:
			december[day] = december[day] + 1
		else:
			december[day] = 1	
		if month==12 and hour in nye:
			nye[hour] = nye[hour] + 1
		else:
			nye[hour] = 1	
plt.bar(range(len(daily)), daily.values(), align='center')
plt.xticks(range(len(daily)), daily.keys())
plt.suptitle('Daily Cycles', fontsize = 14, fontweight='bold')
plt.xlabel('Hour')
plt.ylabel('Number of Timestamps')
plt.show()
for counter in range(1,13):
	month_num = {key[1]: val for key, val in monthly.items() if key[0] == counter}
	plt.bar(range(len(month_num)), month_num.values(), align = 'center')
	plt.xticks(range(len(month_num)), range(24))
	plt.xlabel('Hour')
	plt.ylabel('Number of Timestamps')
	if counter == 7:
		plt.suptitle('July Cycles', fontsize = 14, fontweight='bold')
	elif counter == 8:
		plt.suptitle('August Cycles', fontsize = 14, fontweight='bold')	
	elif counter == 9:
		plt.suptitle('September Cycles', fontsize = 14, fontweight='bold')	
	elif counter == 10:
		plt.suptitle('October Cycles', fontsize = 14, fontweight='bold')	
	elif counter == 11:
		plt.suptitle('November Cycles', fontsize = 14, fontweight='bold')	
	elif counter == 12:
		plt.suptitle('December Cycles', fontsize = 14, fontweight='bold')	
	plt.show()
plt.bar(range(len(december)), december.values(), align='center')
plt.xticks(range(len(december)), december.keys())
plt.suptitle('December daily frequencies', fontsize = 14, fontweight='bold')
plt.xlabel('Day')
plt.ylabel('Number of Timestamps')
plt.show()
plt.bar(range(len(nye)), nye.values(), align='center')
plt.xticks(range(len(nye)), nye.keys())
plt.suptitle('NYE Hourly Requests', fontsize = 14, fontweight='bold')
plt.xlabel('Hour')
plt.ylabel('Number of Timestamps')
plt.show()