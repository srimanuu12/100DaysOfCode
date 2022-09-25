# CSV
#  import csv
# with open("./day_25/weather_data.csv") as f:
#     data = csv.reader(f)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)

import pandas
data = pandas.read_csv("./day_25/weather_data.csv")


# dataframe to dictonary
data_to_dict = data.to_dict()

# Series to list
temp_to_list = data["temp"].to_list

# Average for Temperature column
temp_avg = data["temp"].mean()
# print(temp_avg)

# Maximun value
temp_max = data["temp"].max()
#print(temp_max)

# Get data in columns
#print(data.condition) # It takes condition as attribute
#   or data["condition"]

# Get data in rows
#print(data[data.day == "Monday"])
# get max temperature Row
#print(data[data.temp == data.temp.max()])

# Get monday's temp in F
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * (9/5) +32
# print(monday_temp_f)

# Create dataframe from Scratch
data_dict = {
    "Employees":["Raj","Tom","David","Chandler"],
    "Emp_id": [3495, 4527, 7854, 4961]
}
data2 = pandas.DataFrame(data_dict)
data2.to_csv("./day_25/employee_data.csv")