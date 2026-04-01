#pandas - panel data
#series - 1d array thats can hold any data type . similar to single column in spreadsheet
#dataframe - tabular data structure with rows and colm

import pandas as pd

print(pd.__version__) #-gives current version of pandas

data = [100,102,104]

series = pd.Series(data) # creates a series object with data . pd.Series() is a constructor 
print(series)            # holds array with there index , when printed prints array with their index with the meta data (dtype : int64)
 # we can create custom index for data. 
series2 = pd.Series(data,index=["apartment1","apartment2","apartment3"]) # pd.Series(data,index =[]) value to index can be anything like array , tuple,dictonary etc..
print(series2)      #index= .. this is called the label . label to values 

# accesing data
print(series2.loc["apartment1"]) # series_name.loc[label] - acces data present at the label.
series2.loc["apartment1"] = 300 # can update values using loc fn
series.loc[1] =200  # if no label is manually given then normal 0 based indexing is given to the series
print(series)
print(series2)
print(series2.iloc[2]) # if label is given then also we can access data using 0 based indexing using iloc fn
                       # series_name.iloc[index]-acces data using there index

                       #loc - locate by label and iloc- locate by index


data = [100,102,104,120,201]

series = pd.Series(data,index=["a","b","c","d","e"])

#filtering by value 

print(series[series>=200]) # series_name[condition within series] - filter data based on value.