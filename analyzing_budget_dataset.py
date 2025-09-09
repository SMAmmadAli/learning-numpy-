import pandas as pd

# ------------------------------------------------------------------------------
# Step - 1
# Load and Inspect the Dataset 

# ------------------------
# Load the CSV into a Pandas DataFrame.
# ------------------------

df = pd.read_csv("budget.csv")

# ------------------------
# Check the first few rows to understand the structure.
# ------------------------

print(df.head(3))

# ------------------------
# Inspect column data types
# ------------------------

print("Column Data Types:")
print(df.dtypes)

# ------------------------
# Check for missing value
# ------------------------

print("\nMissing values")
print(df.isnull().sum())

# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------

# step - 2
# Data Cleaning 

# Note:-

'''
errors='coerce': Ye parameter kehta hai ke agar koi value numeric mein convert nahi ho sakti 
(masalan, "abc" ya koi invalid string), to usko NaN (Not a Number) mein badal do. Ye ensure 
karta hai ke column saaf rahe.

format='mixed': Ye parameter kehta hai ke Date column mein dates alag-alag formats mein ho
sakti hain (masalan, "2023-01-01", "01/01/2023", ya "Jan 1, 2023"). format='mixed' ke sath 
Pandas khud hi har date ka format detect karta hai aur usko standard datetime format mein badalta hai.
'
'''

# ------------------------
# Convert the Date column to proper datetime format.
# ------------------------
df["Date"] = pd.to_datetime(df["Date"], format= 'mixed')
df["Date"] = df["Date"].dt.strftime('%Y-%m-%d')  # Specific format mein convert karo

print(df['Date'][10])

# ------------------------
# Ensure Amount is numeric.
# ------------------------

df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

df["Amount"] = pd.to_numeric(df["Amount"].replace('[\$]', '', regex=True), errors='coerce')

# Agar aapko integer chahiye (decimals nahi)
# df["Amount"] = pd.to_numeric(df["Amount"], errors='coerce').astype('Int64')  # Nullable integer type

# print(df["Amount"].to_string())
print(df["Amount"].head(3))

print("Now check the type of amount column")
print(df["Amount"].dtype)

# ------------------------
# Handle missing values
# ------------------------

# Option 1: Drop Rows with Missing Values

# print("Drop null values")
# df.dropna(inplace=True)
# print(df.to_string())
# print(df.isnull().sum())

# Option 2: Fill Missing Values

# print("Fill values in null")

df["Amount"] = df["Amount"].fillna(df["Amount"].mean()) # Mean se fill

# df['Amount'] = df["Amount"].fillna(120) # fill specific value in null

df['Category'] = df["Category"].fillna(df["Category"].mode()[0]) # fill Category through mode()

df["Description"] = df["Description"].fillna("Unknown")

# df["Date"] = df["Date"].fillna("2025-09-09") #apni marzi ke date fill karna
df["Date"] = df["Date"].fillna(method="ffill")  # Previous date se fill
# df["Date"] = df["Date"].fillna(method="bfill")  # Next date se fill

print(df.tail(3))

# -------------------------------------------------------------------------------
