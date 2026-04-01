import pandas as pd

df = pd.read_csv("data.csv")

# selection by column
print(df["Duration"])

print(df[["Duration","Pulse"]]) # can access multiple columns by passing a list of column names


#selection by rows
print(df.loc[0]) # df.loc[label] - can access a row using its label
print(df.iloc[3]) #df.iloc[index] -can access a row using its index

# while importing an csv we can add label to it
df = pd.read_csv("data.csv", index_col ="Duration") ## pd.read_csv("filename",index_col="label col")

print(df.loc[60]) #- access all row with duration 60

#select specific column of row with label
print(df.loc[60,["Maxpulse","Calories"]]) #df.loc[label,[lsit of col]]
# select specific row between a range of label
#df.loc[label start : label end,[lsit of col]]

# select specific row between a range of index
print(df.iloc[34:45]) # df.iloc[start_index,end_index]
print(df.iloc[34:45:2]) # df.iloc[start_index,end_index:step]
#can also pass number of columns as second argument
print(df.iloc[2:45,0:2]) #df.iloc[start_index,end_index:step, startindexofcolumn:endindofcol]


