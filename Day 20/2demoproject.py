import pandas as pd
 

df = pd.read_csv("sales.csv")

# print(df)
#    Order_ID        Date    City Category    Sales
# 1       102  2026-01-08   Delhi   Mobile  30000.0
# 2       103  2026-02-10  Indore   Laptop  45000.0
# 3       104  2026-02-15  Indore   Mobile  25000.0
# 4       105  2026-03-02  Bhopal   Laptop  47000.0
# 5       106  2026-03-12  Bhopal   Mobile      NaN
# 6       107  2026-04-05   Delhi   Laptop  52000.0
# 7       108  2026-04-18  Indore   Mobile  27000.0
# 8       109  2026-05-01  Bhopal   Laptop  49000.0
# 9       110  2026-05-20   Delhi   Mobile  32000.0

#Basic Information
# print(df.head(5))
#    Order_ID        Date    City Category    Sales
# 0       101  2026-01-05   Delhi   Laptop  50000.0
# 1       102  2026-01-08   Delhi   Mobile  30000.0
# 2       103  2026-02-10  Indore   Laptop  45000.0
# 3       104  2026-02-15  Indore   Mobile  25000.0
# 4       105  2026-03-02  Bhopal   Laptop  47000.

# print(df.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 5 columns):
#  #   Column    Non-Null Count  Dtype  
# ---  ------    --------------  -----  
#  0   Order_ID  10 non-null     int64  
#  1   Date      10 non-null     str    
#  2   City      10 non-null     str    
#  3   Category  10 non-null     str    
#  4   Sales     9 non-null      float64
# dtypes: float64(1), int64(1), str(3)
# memory usage: 532.0 bytes
# None

# print(df.describe())
#         Order_ID         Sales
# count   10.00000      9.000000
# mean   105.50000  39666.666667
# std      3.02765  10931.605555
# min    101.00000  25000.000000
# 25%    103.25000  30000.000000
# 50%    105.50000  45000.000000
# 75%    107.75000  49000.000000
# max    110.00000  52000.000000

#Missing Values
# print(df.isnull().sum())
# Order_ID    0
# Date        0
# City        0
# Category    0
# Sales       1
# dtype: int64

#Fill Missing Sales
# df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
# print(df)
#    Order_ID        Date    City Category         Sales
# 0       101  2026-01-05   Delhi   Laptop  50000.000000
# 1       102  2026-01-08   Delhi   Mobile  30000.000000
# 2       103  2026-02-10  Indore   Laptop  45000.000000
# 3       104  2026-02-15  Indore   Mobile  25000.000000
# 4       105  2026-03-02  Bhopal   Laptop  47000.000000
# 5       106  2026-03-12  Bhopal   Mobile  39666.666667
# 6       107  2026-04-05   Delhi   Laptop  52000.000000
# 7       108  2026-04-18  Indore   Mobile  27000.000000
# 8       109  2026-05-01  Bhopal   Laptop  49000.000000
# 9       110  2026-05-20   Delhi   Mobile  32000.000000

#Convert Date
df["Date"] = pd.to_datetime(df["Date"])

#New Columns
# df["Month"] = df["Date"].dt.month
# print(df)
#    Order_ID       Date    City Category    Sales  Month
# 0       101 2026-01-05   Delhi   Laptop  50000.0      1
# 1       102 2026-01-08   Delhi   Mobile  30000.0      1
# 2       103 2026-02-10  Indore   Laptop  45000.0      2
# 3       104 2026-02-15  Indore   Mobile  25000.0      2
# 4       105 2026-03-02  Bhopal   Laptop  47000.0      3
# 5       106 2026-03-12  Bhopal   Mobile      NaN      3
# 6       107 2026-04-05   Delhi   Laptop  52000.0      4
# 7       108 2026-04-18  Indore   Mobile  27000.0      4
# 8       109 2026-05-01  Bhopal   Laptop  49000.0      5
# 9       110 2026-05-20   Delhi   Mobile  32000.0      5

# df["Year"] = df["Date"].dt.year
# print(df)
#    Order_ID       Date    City Category    Sales  Year
# 0       101 2026-01-05   Delhi   Laptop  50000.0  2026
# 1       102 2026-01-08   Delhi   Mobile  30000.0  2026
# 2       103 2026-02-10  Indore   Laptop  45000.0  2026
# 3       104 2026-02-15  Indore   Mobile  25000.0  2026
# 4       105 2026-03-02  Bhopal   Laptop  47000.0  2026
# 5       106 2026-03-12  Bhopal   Mobile      NaN  2026
# 6       107 2026-04-05   Delhi   Laptop  52000.0  2026
# 7       108 2026-04-18  Indore   Mobile  27000.0  2026
# 8       109 2026-05-01  Bhopal   Laptop  49000.0  2026
# 9       110 2026-05-20   Delhi   Mobile  32000.0  2026

#Highest Sale
# print(df["Sales"].max())
# 52000.0

#Highest Sale all details
# print(df.sort_values(["Sales"], ascending=False).head(1))
#    Order_ID       Date   City Category    Sales
# 6       107 2026-04-05  Delhi   Laptop  52000.0

#Delhi Sales
# print(df[df["City"] == "Delhi"])
#    Order_ID       Date   City Category    Sales
# 0       101 2026-01-05  Delhi   Laptop  50000.0
# 1       102 2026-01-08  Delhi   Mobile  30000.0
# 6       107 2026-04-05  Delhi   Laptop  52000.0
# 9       110 2026-05-20  Delhi   Mobile  32000.0

#Category Wise Sales
# print(df.groupby("Category")["Sales"].mean())
# Category
# Laptop    48600.0
# Mobile    28500.0
# Name: Sales, dtype: float64

#Pivot Table
# print(
#     pd.pivot_table(
#         df,
#         values="Sales",
#         index=["City", "Category"],
#         aggfunc="sum",
#         margins=True
#     )
# )

#                     Sales
# City   Category          
# Bhopal Laptop     96000.0
#        Mobile         0.0
# Delhi  Laptop    102000.0
#        Mobile     62000.0
# Indore Laptop     45000.0
#        Mobile     52000.0
# All              357000.0

#Performance Column
# df["Performance"] = df["Sales"].apply(
#     lambda x: "High" if x >= 40000 else "Low"
# )
# print(df)
#    Order_ID       Date    City Category    Sales Performance
# 0       101 2026-01-05   Delhi   Laptop  50000.0        High
# 1       102 2026-01-08   Delhi   Mobile  30000.0         Low
# 2       103 2026-02-10  Indore   Laptop  45000.0        High
# 3       104 2026-02-15  Indore   Mobile  25000.0         Low
# 4       105 2026-03-02  Bhopal   Laptop  47000.0        High
# 5       106 2026-03-12  Bhopal   Mobile      NaN         Low
# 6       107 2026-04-05   Delhi   Laptop  52000.0        High
# 7       108 2026-04-18  Indore   Mobile  27000.0         Low
# 8       109 2026-05-01  Bhopal   Laptop  49000.0        High
# 9       110 2026-05-20   Delhi   Mobile  32000.0         Low

#Running Total
# df["Running_Total"] = df["Sales"].cumsum()
# print(df)
#    Order_ID       Date    City Category    Sales  Running_Total
# 0       101 2026-01-05   Delhi   Laptop  50000.0        50000.0
# 1       102 2026-01-08   Delhi   Mobile  30000.0        80000.0
# 2       103 2026-02-10  Indore   Laptop  45000.0       125000.0
# 3       104 2026-02-15  Indore   Mobile  25000.0       150000.0
# 4       105 2026-03-02  Bhopal   Laptop  47000.0       197000.0
# 5       106 2026-03-12  Bhopal   Mobile      NaN            NaN
# 6       107 2026-04-05   Delhi   Laptop  52000.0       249000.0
# 7       108 2026-04-18  Indore   Mobile  27000.0       276000.0
# 8       109 2026-05-01  Bhopal   Laptop  49000.0       325000.0
# 9       110 2026-05-20   Delhi   Mobile  32000.0       357000.0

# df["Rolling_Average"]   = df["Sales"].rolling(3).mean()
# print(df)
#    Order_ID       Date    City Category    Sales  Rolling_Average
# 0       101 2026-01-05   Delhi   Laptop  50000.0              NaN
# 1       102 2026-01-08   Delhi   Mobile  30000.0              NaN
# 2       103 2026-02-10  Indore   Laptop  45000.0     41666.666667
# 3       104 2026-02-15  Indore   Mobile  25000.0     33333.333333
# 4       105 2026-03-02  Bhopal   Laptop  47000.0     39000.000000
# 5       106 2026-03-12  Bhopal   Mobile      NaN              NaN
# 6       107 2026-04-05   Delhi   Laptop  52000.0              NaN
# 7       108 2026-04-18  Indore   Mobile  27000.0              NaN
# 8       109 2026-05-01  Bhopal   Laptop  49000.0     42666.666667
# 9       110 2026-05-20   Delhi   Mobile  32000.0     36000.000000

#Create Grade
# def grade(x):
#     if x >= 50000:
#         return "A"
#     elif x >= 40000:
#         return "B"
#     else:
#         return "C"
    
# df["Grade"] = df["Sales"].apply(grade)
# print(df)
#    Order_ID       Date    City Category    Sales Grade
# 0       101 2026-01-05   Delhi   Laptop  50000.0     A
# 1       102 2026-01-08   Delhi   Mobile  30000.0     C
# 2       103 2026-02-10  Indore   Laptop  45000.0     B
# 3       104 2026-02-15  Indore   Mobile  25000.0     C
# 4       105 2026-03-02  Bhopal   Laptop  47000.0     B
# 5       106 2026-03-12  Bhopal   Mobile      NaN     C
# 6       107 2026-04-05   Delhi   Laptop  52000.0     A
# 7       108 2026-04-18  Indore   Mobile  27000.0     C
# 8       109 2026-05-01  Bhopal   Laptop  49000.0     B
# 9       110 2026-05-20   Delhi   Mobile  32000.0     C

#Top 3 Sales
# print(df.nlargest(
#     3,
#     "Sales"
#   )
# ) also smallest
#    Order_ID       Date    City Category    Sales
# 6       107 2026-04-05   Delhi   Laptop  52000.0
# 0       101 2026-01-05   Delhi   Laptop  50000.0
# 8       109 2026-05-01  Bhopal   Laptop  49000.0