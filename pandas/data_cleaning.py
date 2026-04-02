import pandas as pd

#data cleaning - the process of fixing/removing : incomplete.incorrect,or irrelevent data.

df = pd.read_csv("pokemon.csv")

# drop irrevent column
df = df.drop(columns=["Legendary","No"])
#- dataframe_name.drop(columns=[list of column to remove]) - returns a new data frame after removing the given columns


# hadle missing data
#here we will drop all the rows which dont have type2
# df = df.dropna(subset=["Type2"]) #dropna(subset=[list of columns(which has empty empty)])
df = df.fillna({"Type2" : "None"}) #fillna({name of col : value to fill}) - fill the given value ar everyplace where given column has value none


#fix inconsistent values
df["Type1"] = df["Type1"].replace({"Grass" : "GRASS"}) # df[columnname].replace({oldvalue : newvalue}) - replaces the old value in the given column with new value
# we can pass mutliple values to change its value
df["Type1"] = df["Type1"].replace({"Grass" : "GRASS" , "Fire":"FIRE"}) ## df[columnname].replace({oldvalue : newvalue,oldvalue:newvalue,....})


# standardize text
df["Name"] = df["Name"].str.lower()



# fix data types
df = pd.read_csv("pokemon.csv")
df["Legendary"] = df["Legendary"].astype(bool) #df["colname"].astype(new data type)


# removing duplicate values
df = df.drop_duplicates();


print(df)