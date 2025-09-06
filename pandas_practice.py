import pandas as pd 

print(pd.__version__)


py_dict = {
    "name" : ["Ammad", "Shaheer", "Aliyan", "Anas"],
    "number" : [93,73, 38, 24],
    "subject" : ["Math", "Physics", "Chemistry", "DIP"]
}

df = pd.DataFrame(py_dict)

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

# up_anas = read_file["number"][3]

# up_anas = 52


# update_col = up_anas

# print(update_col)

print(read_file)
print("----------------------------------------------------")
# Anas ka number update karein
read_file.loc[3, "number"] = 51

# Ammad ka name update karein
read_file.loc[0, "name"] = "Syed Ammad"

# "Aliyan" ka row dhoondho aur number update karo

read_file.loc[read_file["name"] == "Aliyan", "number"] = 53

# Case-insensitive tareeke se Aliyan dhoondho aur number update karo
read_file.loc[read_file["name"].str.lower() == "shaheer", "number"] = 80

print(read_file)


# add new row on csv file

# create new dict
new_row = {
    "name": ["Syed Aliyan", "Aliyan"],
    "number": [83, 76],
    "subject": ["ToA", "DAA"]
}

# Row add karo using concat

read_file = pd.concat([read_file, pd.DataFrame(new_row)], ignore_index=True)

print("-----------------------Updated Sheet-----------------------------")

print(read_file)

print("----------------------------------------------------")


# Sirf us Aliyan ka number update karo jiska subject Chemistry hai

read_file.loc[(read_file["name"] == "Aliyan") & (read_file['subject'] == "DAA"), "number"] = 42
print(read_file)
