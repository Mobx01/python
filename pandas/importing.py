import pandas as pd

# load csv file :- pd.read_csv(path)
df = pd.read_csv("data.csv") #-

print(df) # only gives first and last 5 data
print(df.to_string()) #- prints all the data

# df = pd.read_json("path of json file") - reads json file and save the dataframe in the given variable
