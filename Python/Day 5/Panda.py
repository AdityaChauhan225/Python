#pandas
"""
It is an open source python library used for data manupulation and anylysis.
It provides data structures like dataframes and series (which are designes to handle tabuler and timeseries data efficiently.)
stands for python data anaylsis
It is not a database but it can work with data from various souces such as CSV files , Excel files and SQL database
"""

import pandas as pd
import numpy as np
# Series
''' 
It is a one dimentional labled array which can store any datatype.
It consists of value and lables ( index )  
'''
s  = pd.Series(["Aadi","Aayu","Sdi"],index =[1,2,3])
print(s)
print(s.values)


#DataFrame

'''
Dataframe is a two dimentional table which consist of rows, columns and it offers lables 
'''

data = { 
    "name":["alice","bob","charlie"],
    "Age" : [25,30,35],
    "Score":[85,90,95]
}

df = pd.DataFrame(data)
print(df)

# print(df.head()) # returns first 5 rows of df
# print(df.tail()) # returns last 5 rows of df

print(df.loc[0])
print(df[df["Score"]>85])

df["Grade"]=["B","A","A+"]
print(df)
df.drop("Age",axis=1,inplace=True)
print(df)
df.rename(columns={"Score":"Marks"},inplace=True)
print(df)


df1 = pd.DataFrame({
    "Name": ["Alice",None,"Charlie"],
    "Marks":[85, np.nan, 95]
})

print(df1.isnull()) # returns true in place of none values and false in 
df1.fillna("unknown",inplace=True) # Replaces none values with provided
print(df1)
df1.dropna(inplace=True) # deletes none values

print(df.describe())     # summary text
print(df.mean(numeric_only=True))    #  Mean for numeric columns
print(df.groupby("Grade")["Marks"].mean() ) # groupping

print(df[0:2])

df.set_index("name",inplace=True)
print(df)

df.reset_index(inplace=True)
print(df)

## CSV

'''
CSV stands for Comma Seperated Values
a simple way to store big data 
it contains plain text and can be read using pandas
'''

df2=pd.read_csv("day.csv")
print(df2.head())

df.to_csv("Output.csv",index=False)


# df2=pd.read_excel("data.xlsx")
# df.to_excel("Output.csv")


s= pd.Series([1,2,3],index=["alice","bob","charlie"])
print(s[["alice","bob"]])
print(s)
print(s.values)
print(s.size)
print(s.shape)
s["charlie"] = 4
print(s)
s.drop("charlie", inplace=True)

s1=pd.Series([1,2,3])
print(s1+2)
print(s1*10)
print(s1**2)
print(s1[s1>2])

print(s1.sum())
print(s1.mean())
print(s1.min(),s1.max())
print(s1.std())             #standard deviation

names = pd.Series(["alice","bob","CHARLIE","dave"])
print(names.str.upper())
print(names.str.capitalize())
print(names.str.contains("a"))


s = pd.Series([30,10,40,20],index=["d","b",'a','c'])
print(s.sort_values()) # Sort by values
print(s.sort_index())  # Sort by index
print(s.rank())

s1 = pd.Series([10,20,30],index=['a','b','c'])
s2 = pd.Series([5,15,25],index=['b','c','d'])
print(s1+s2)
