# with open('weather_data.csv') as weather_file:
#     weather = weather_file.readlines()
# import csv
# with open('weather_data.csv') as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd
# data = pd.read_csv('weather_data.csv')
# # temp_mean = data['temp'].mean()
# # print(temp_mean)
# # print(data[data.temp == data.temp.max()])
# # temp_max = data['temp'].max()
# # print(temp_max)
#
# # Monday temp from C to F
# # monday = data[data.day == 'Monday']
# # monday_temp = int(monday.temp)
# # temp_f = ((monday_temp * 9/5) + 32)
# # print(temp_f)
#
# # Create a DF from scratch
# data_dct = {
#     'students': ['Amy', 'Jmaes', 'chris'],
#     'scores': [90, 40, 80]
# }
#
# data = pd.DataFrame(data_dct)
# data.to_csv('new_data.csv')
sq_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color = sq_data['Primary Fur Color']

# print(color)
gray_sq = len(sq_data[sq_data['Primary Fur Color'] == 'Gray'])
cinnamon_sq = len(sq_data[sq_data['Primary Fur Color'] == 'Cinnamon'])
black_sq = len(sq_data[sq_data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Primary Fur Color": ['gray', 'cinnamon', 'black'],
    'Count': [gray_sq, cinnamon_sq, black_sq]
}
df = pd.DataFrame(data_dict)
df.to_csv('squirrel_count_by_color.csv')