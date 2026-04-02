import pandas as pd

# Aggregate function -reduces a set of values into a single summary value
#                     used to summarize and analyze data
                    #often used with groupby() function

#dataframe_name.mean() - finds mean of each column passed (if non then for all) . but it can't find mean of non numeric values so use this as solution
# sol- dataframe_name.mean(numeric_only =True).

df = pd.read_csv("pokemon.csv")

#print(df.mean()) - will throw error because a non numeric column was passed
print(df.mean(numeric_only=True))


#dataframe_name.sum() - finds sum of each column passed (if non then for all) . but it will concatenate all the strings for a column if the column is of strings
# sol- dataframe_name.sum(numeric_only =True).
print(df.sum())
print(df.sum(numeric_only=True))

#dataframe_name.min() - finds min of each column passed (if non then for all) . but it will return string which is  lexiographically minimum
print(df.min())
print(df.min(numeric_only=True))

#dataframe_name.max() - finds maximum of each column passed (if non then for all) . but it will return string which is  lexiographically maximum
print(df.max())
print(df.max(numeric_only=True))

#dataframe_name.count() - counts number of element in the column
print(df.count())


#isngle column

print(df["Height"].mean())
print(df["Weight"].sum())
print(df["Height"].min())
print(df["Weight"].max())
print(df["Type2"].count())

#dataframe_name.groupby(column name) - creates an object of group grouping by column name passed as argument
#                                    - returns an series after grouping
group = df.groupby("Type1")

print(group["Height"].mean()) # return avg height of each type
print(group["Height"].sum())  # return sum of height of each type
print(group["Height"].count())  # return number of pkemon of each type
