import pandas
# data = pandas.read_csv("weather_data.csv")
# temps = data["temp"].to_list()

# average_temp = sum(temps) / len(temps)
# print(average_temp)

# mean = data["temp"].mean()
# largest =data["temp"].max()

# get Data in columns
# print(data["condition"])
# print(data.condition)

# get Data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# tuesday = data[data.day == "Tuesday"]
#
# print((monday.temp.item() * 1.8) + 32)
# print((tuesday.temp.iloc[0] * 1.8) + 32)


# create dataframe from scratch
# data_dict ={
#     "students":["Prikkel","Matisse","Bob",],
#     "scores":[85,93, 55]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "black"])


colors = data["Primary Fur Color"].to_list()
gray = colors.count("Gray")
cinnamon = colors.count("Cinnamon")
black =  colors.count("Black")

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon","Black"],
    "Count": [gray,cinnamon,black],
}
counts = data["Primary Fur Color"].value_counts()
print(counts)
# dataframe = pandas.DataFrame(squirrel_dict)
# dataframe.to_csv("squirrel_color_count.csv")