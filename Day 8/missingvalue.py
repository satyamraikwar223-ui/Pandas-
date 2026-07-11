
from pathlib import Path
import pandas as pd

# use a path string for the folder name "Day 8"
df = pd.read_csv(Path("Day 8") / "missing.csv")

# print(df)
# output:
#       Name   Age       City  Marks
# 0   Satyam  18.0  Khajuraho   90.0
# 1   Shivam   NaN     Indore   85.0
# 2  Lakshya  19.0        NaN   88.0
# 3    Rahul  21.0      Delhi    NaN

# print(df.isnull()) #print true for missing values and false for non-missing values
# output:
#     Name    Age   City  Marks
# 0  False  False  False  False
# 1  False   True  False  False
# 2  False  False   True  False
# 3  False  False  False   True

# print(df.isnull().sum()) #print the count of missing values in each column
# output:
# Name     0
# Age      1
# City     1
# Marks    1
# dtype: int64

# print(df.notnull()) #print true for non-missing values and false for missing values
# output:
#    Name    Age   City  Marks
# 0  True   True   True   True
# 1  True  False   True   True
# 2  True   True  False   True
# 3  True   True   True  False

# df["Age"] = df["Age"].fillna(18, inplace=True) #fill missing values in Age column with 18
# print(df)
# output:
#       Name   Age       City  Marks
# 0   Satyam  18.0  Khajuraho   90.0
# 1   Shivam  18.0     Indore   85.0
# 2  Lakshya  19.0        NaN   88.0
# 3    Rahul  21.0      Delhi    NaN

# df["City"] = df["City"].fillna("Bhopal", inplace=True) #fill missing values in City column with Bhopal
# print(df)
# output:
#       Name   Age       City  Marks
# 0   Satyam  18.0  Khajuraho   90.0
# 1   Shivam   NaN     Indore   85.0
# 2  Lakshya  19.0     Bhopal   88.0
# 3    Rahul  21.0      Delhi    NaN

# average = df["Marks"].mean() #calculate the average of Marks column
# df["Marks"] = df["Marks"].fillna(average, inplace=True) #fill missing values in Marks column with average
# print(df)
# output:
#       Name   Age       City      Marks
# 0   Satyam  18.0  Khajuraho  90.000000
# 1   Shivam   NaN     Indore  85.000000
# 2  Lakshya  19.0        NaN  88.000000
# 3    Rahul  21.0      Delhi  87.666667


# print(df.dropna()) #drop rows with missing values
# output:
#      Name   Age       City  Marks
# 0  Satyam  18.0  Khajuraho   90.0

# print(df[df["Age"].isnull()]) #print rows with missing values in Age column
# putput:
#      Name  Age    City  Marks
# 1  Shivam  NaN  Indore   85.0

# print(df[df["City"].notnull()]) #print rows with non-missing values in City column
# output:
#     Name   Age       City  Marks
# 0  Satyam  18.0  Khajuraho   90.0
# 1  Shivam   NaN     Indore   85.0
# 3   Rahul  21.0      Delhi    NaN

#print((df.isnull().sum() / len(df)) * 100)
# output:
# Name      0.0
# Age      25.0
# City     25.0
# Marks    25.0
# dtype: float64

# print(df["City"].dropna())
# output:
# 0    Khajuraho
# 1       Indore
# 3        Delhi
# Name: City, dtype: str

# print(df[df["City"].isnull()]) #print only row in which city is missing
# output:
#       Name   Age City  Marks
# 2  Lakshya  19.0  NaN   88.0

 