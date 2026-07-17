import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman","Rohit","Neha","Priya"],
    "Joining_Date": [
        "2022-01-15",
        "2021-08-20",
        "2023-03-12",
        "2020-11-05"
    ]
})

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])
 
# print(df)
# output:
#     Name Joining_Date
# 0   Aman   2022-01-15
# 1  Rohit   2021-08-20
# 2   Neha   2023-03-12
# 3  Priya   2020-11-05

# print(df["Joining_Date"].dt.year)
# output:
# 0    2022
# 1    2021
# 2    2023
# 3    2020
# Name: Joining_Date, dtype: int32

# print(df["Joining_Date"].dt.day)
# # output:
# 0    15
# 1    20
# 2    12
# 3     5
# Name: Joining_Date, dtype: int32

# print(df["Joining_Date"].dt.month)
#  # output:
#  0     1
# 1     8
# 2     3
# 3    11
# Name: Joining_Date, dtype: int32


# print(df["Joining_Date"].dt.day_name())
#  # output:
#  0    Saturday
# 1      Friday
# 2      Sunday
# 3    Thursday
# Name: Joining_Date, dtype: str

# print(df["Joining_Date"].dt.month_name())
#  # output:
# 0     January
# 1      August
# 2       March
# 3    November
# Name: Joining_Date, dtype: str

# print(df["Joining_Date"].dt.weekday)
# # output:
# 0    5
# 1    4
# 2    6
# 3    3
# Name: Joining_Date, dtype: int32

# print(df[df["Joining_Date"] > "2020-11-05"])
# output:
#     Name Joining_Date
# 0   Aman   2022-01-15
# 1  Rohit   2021-08-20
# 2   Neha   2023-03-12


# today = pd.Timestamp("2026-07-17")

# df["Days_Passed"] = today - df["Joining_Date"]

# print(df)
# output:
#     Name Joining_Date Days_Passed
# 0   Aman   2022-01-15   1644 days
# 1  Rohit   2021-08-20   1792 days
# 2   Neha   2023-03-12   1223 days
# 3  Priya   2020-11-05   2080 days


# df["Year"] = df["Joining_Date"].dt.year
# df["Month"] = df["Joining_Date"].dt.month
# df["Month_name"] = df["Joining_Date"].dt.month_name()
# df["Day"] = df["Joining_Date"].dt.day
# df["Day_name"] = df["Joining_Date"].dt.day_name()
# df["Weekday"] = df["Joining_Date"].dt.weekday

#print(df) 
# output; df["new colom name"] 
#     Name Joining_Date  Year  Month Month_name  Day  Day_name  Weekday
# 0   Aman   2022-01-15  2022      1    January   15  Saturday        5
# 1  Rohit   2021-08-20  2021      8     August   20    Friday        4
# 2   Neha   2023-03-12  2023      3      March   12    Sunday        6
# 3  Priya   2020-11-05  2020     11   November    5  Thursday        3

#print(df.groupby("Day").size())

#print(df.sort_values("Joining_Date").head(2, accending=False))

#print(df["Name"].str.capitalize())
