from cgitb import grey
import pandas

data = pandas.read_csv("./day_25/Squirrel/2018_centralpark_Squirrel_Data.csv")
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count]
}

squirrel_data = pandas.DataFrame(squirrel)
squirrel_data.to_csv("./day_25/Squirrel/squirrel_count.csv")