import pandas as pd 

print(pd.__version__)


py_dict = {
    "name" : ["Ammad", "Shaheer", "Aliyan", "Anas"],
    "number" : [93,73, 38, 24],
    "subject" : ["Math", "Physics", "Chemistry", "DIP"]
}

# df = pd.DataFrame(py_dict)

# print(df)

# df.to_csv("result.csv", index=False)

# print(df.head(2))

# print(df.tail(2))

# print(df.describe())


# CSV file read karein
read_file = pd.read_csv("result.csv", index_col= 0)

# print(read_file)

# print(read_file["number"])
# print(read_file["number"][3])


# print("----------------------------------------------------")
# Anas ka number update karein
read_file.loc[3, "number"] = 51

# Ammad ka name update karein
read_file.loc[0, "name"] = "Syed Ammad"

# "Aliyan" ka row dhoondho aur number update karo

read_file.loc[read_file["name"] == "Aliyan", "number"] = 53

# Case-insensitive tareeke se Aliyan dhoondho aur number update karo
read_file.loc[read_file["name"].str.lower() == "shaheer", "number"] = 80

# print(read_file)


# add new row on csv file

# create new dict
new_row = {
    "name": ["Syed Aliyan", "Aliyan"],
    "number": [83, 76],
    "subject": ["ToA", "DAA"]
}

# Row add karo using concat

read_file = pd.concat([read_file, pd.DataFrame(new_row)], ignore_index=True)

# print("-----------------------Updated Sheet-----------------------------")

# print(read_file)

# print("----------------------------------------------------")


# Sirf us Aliyan ka number update karo jiska subject Chemistry hai

read_file.loc[(read_file["name"] == "Aliyan") & (read_file['subject'] == "DAA"), "number"] = 42
# print(read_file)

# Number ke hisaab se descending order mein sort karo
read_file = read_file.sort_values(by="number", ascending=False, ignore_index=True)

read_file.to_csv("update result.csv")


# Series

# A Pandas Series is like a column in a table.

# It is a one-dimensional array holding data of any type.

# print("----------------------Series------------------------------")


a = [2,4,"a", 3.5]

to_series = pd.Series(a)

# print(to_series)
# print(to_series[2])

series_with_Label = pd.Series(a, index= ['a',"b","c",'d'])
# print(series_with_Label)
# print(series_with_Label["d"])


# Dictionary

calories = {"day1" : 420, "day2" : 380, "day3": 360}

cal = pd.Series(calories)

# print(cal)


# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

# Series is like a column, a DataFrame is the whole table.

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

# print(myvar)

data_file = pd.read_csv("data.csv")

# print(f"max rows: {pd.options.display.max_rows}") 
# print(data_file.to_string())

# print(data_file.head(4))

# print(data_file.tail(4))


# Read Json 
read_json = pd.read_json("json_data.json")

# print(read_json.to_string())


# Pandas Analyzing DataFram

# print(data_file.head())

# print(data_file.tail())

# print(data_file.info())

# print(data_file.describe())



# Pandas Cleaning Data
'''
Data cleaning means fixing bad data in your data set.

Bad data could be:

Empty cells
Data in wrong format
Wrong data
Duplicates

'''

# 1- empty cells

# remove rows that contain empty cells

# Return a new Data Frame with no empty cells:

df = pd.read_csv("data.csv")

# df.dropna(inplace=True)
"""
 By default, the dropna() method returns a new DataFrame, and will not change the original.

 If you want to change the original DataFrame, use the inplace = True argument

 Now, the dropna(inplace = True) will NOT return a new DataFrame, 
 but it will remove all rows containing NULL values from the original DataFrame.
 """

# Replace NULL values with values

df.fillna("Ammad", inplace=True)

# print(df.to_string())

result = df[df["Calories"].str.lower() == "ammad"]


# print(result)


df.to_csv("data1.csv")

# Data of Wrong Format

# print(df.head())

# Detect duplicate

# print(df.duplicated())
