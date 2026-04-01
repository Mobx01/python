import pandas as pd

data = {"Name" :["spongbob","patrick","squidward"],
        "Age":[30,35,50]
        }

df = pd.DataFrame(data) #pd.DataFrame() is a constructre which initialises an object of dataframe 
print(df)

# we can also assgin custom label(index)
df = pd.DataFrame(data,index=["emp 1","emp 2","emp3"])#syntax- pd.DataFrame(data,index=[values of index])
print(df)


print(df.loc["emp 1"]) # accesing data by label dataframe_name.loc[label]
 
print(df.iloc[0]) # accesing data by 0 based index

#add a new column
#syntax - dataframe_name["new_col_name"] =[value] , the list of values must have same number values as of rows
df["job"] = ["cook","technician","cashier"]
print(df)
# add a new row- make a new data frame and concatenate it with old one
new_row = pd.DataFrame([{"Name" : "sanda","Age" : 28,"job": "janitor"}],   index =["emp4"])

df = pd.concat([df,new_row])  #pd.concat([list of dataframe to be concatinated]) - concatenates dataframes
print(df)
# we can add multiple rows just make list  of rows while maling a new dataframe
# eg- pd.DataFrame([{},{},{},...])


