# Importing libraries
import pandas as pd

# Read csv file into a pandas dataframe
df = pd.read_csv("employees.csv")
print(df.head())
print("after:")
# a list with all missing value formats
missing_value_formats = ["n.a.","?","NA","n/a", "na", "--","-","n.a"]
df = pd.read_csv("employees.csv", na_values = missing_value_formats)

# print gender again
print(df.head())