import pandas as pd

#this dictonory stores amounnt of calories consumed on the day
calories = {"Day 1" : 1750, "Day 2": 2100 ,"Day 3":1700}

series = pd.Series(calories)
print(series)
print(series.loc["Day 3"])
#if my goal is to eat less than 2000 calories so i have to found on which day i failes
print(series[series > 2000]) 
#days i follow the plan
print(series[series < 2000])