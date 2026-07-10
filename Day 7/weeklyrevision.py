import pandas as pd
from pathlib import Path

df = pd.read_csv(Path("Day 7") / "students.csv")

# print(df)
# output:

#       Name  Age       City  Marks
# 0   Satyam   18  Khajuraho     91
# 1   Shivam   20     Indore     85
# 2  Lakshya   18     Bhopal     88
# 3    Rahul   19      Delhi     79
# 4     Aman   21    Gwalior     92
# 5    Rohit   20   Jabalpur     81
# 6    Priya   19      Sagar     95
# 7     Neha   18     Ujjain     87
# 8    Karan   21       Rewa     84
# 9   Anjali   20      Satna     90

# print(df.dtypes)
# output:
# Name       str
# Age      int64
# City       str
# Marks    int64
# dtype: object

# print(df.describe())
# output:
#              Age      Marks
# count  10.000000  10.000000
# mean   19.400000  87.200000
# std     1.173788   5.028806
# min    18.000000  79.000000
# 25%    18.250000  84.250000
# 50%    19.500000  87.500000
# 75%    20.000000  90.750000
# max    21.000000  95.000000

# print(df.info())
# output:
# <class 'pandas.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Name    10 non-null     str  
#  1   Age     10 non-null     int64
#  2   City    10 non-null     str  
#  3   Marks   10 non-null     int64
# dtypes: int64(2), str(2)
# memory usage: 452.0 bytes
# None

# print(df.shape)
# output:
# (10, 4)

# print(df.columns)
#output:
# Index(['Name', 'Age', 'City', 'Marks'], dtype='str')

# print(df.head(2))
# output:

#      Name  Age       City  Marks
# 0  Satyam   18  Khajuraho     91
# 1  Shivam   20     Indore     85

# print(df.sort_values("Marks", ascending=False).head(1))
# output:
#     Name  Age   City  Marks
# 6  Priya   19  Sagar     95

# print(df[df["Marks"]> 90])
# output:

#      Name  Age       City  Marks
# 0  Satyam   18  Khajuraho     91
# 4    Aman   21    Gwalior     92
# 6   Priya   19      Sagar     95

# print(df[df["City"] == "Indore"].sort_values("Marks", ascending=False).head(1))
# output:
#      Name  Age    City  Marks
# 1  Shivam   20  Indore     85

# print(df[df["Age"] >= 20][["Name", "Marks"]])
# output:

#      Name  Marks
# 1  Shivam     85
# 4    Aman     92
# 5   Rohit     81
# 8   Karan     84
# 9  Anjali     90

# print(df[df["City"] == "Bhopal"])
# output:
#       Name  Age    City  Marks
# 2  Lakshya   18  Bhopal     88

# print(df.loc[0])
# output:
# Name        Satyam
# Age             18
# City     Khajuraho
# Marks           91
# Name: 0, dtype: object

# print(df.loc[0, "Name"])
# output:
# Satyam

#print(df.iloc[0])
# output:
# Name        Satyam
# Age             18
# City     Khajuraho
# Marks           91
#Name: 0, dtype: object

#print(df.iloc[0, 0])
# output:
# Satyam

