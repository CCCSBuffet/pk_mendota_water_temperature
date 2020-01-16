import csv
from matplotlib import pyplot as plt 

input_file = open('may_6.csv')
reader = csv.reader(input_file)

yearly_data = {}

for line in reader:
    year = line[0][0:4]
    if year not in yearly_data:
        yearly_data[year] = { }
    yearly_data[year][float(line[1])] = float(line[2])


for year in sorted(yearly_data):
    depths = sorted(list(yearly_data[year]))
    temps = []
    for d in depths:
        temps.append(yearly_data[year][d])
    plt.plot(depths, temps, label='5/6/' + str(year))

plt.style.use('fivethirtyeight')
plt.legend()
plt.title('Lake Mendota - Madison, WI')
plt.xlabel('Depth (Feet)')
plt.ylabel('Temperature (C)')
plt.show()

