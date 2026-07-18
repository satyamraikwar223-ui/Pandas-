import pandas as pd

student = {
    "Name": [
        "Aman","Rohit","Neha","Priya","Arjun",
        "Sneha","Karan","Pooja","Vivek","Anjali"
    ],
    "City": [
        "Delhi","Indore","Delhi","Bhopal","Indore",
        "Delhi","Bhopal","Indore","Delhi","Bhopal"
    ],
    "Marks":[
        85,90,78,95,88,
        None,91,84,76,89
    ],
    "Age":[
        18,19,18,20,19,
        18,20,19,18,20
    ],
    "Joining_Date":[
        "2026-01-10",
        "2026-02-15",
        "2026-03-20",
        "2026-01-25",
        "2026-04-10",
        "2026-05-12",
        "2026-02-28",
        "2026-03-18",
        "2026-01-05",
        "2026-06-01"
    ]
}

df = pd.DataFrame(student)

#Display first 5 rows.
# print(df.head(5))
# #     Name    City  Marks  Age Joining_Date
# # 0   Aman   Delhi   85.0   18   2026-01-10
# # 1  Rohit  Indore   90.0   19   2026-02-15
# # 2   Neha   Delhi   78.0   18   2026-03-20
# # 3  Priya  Bhopal   95.0   20   2026-01-25
# # 4  Arjun  Indore   88.0   19   2026-04-10

# #print imformation
# print(df.info())
# # <class 'pandas.DataFrame'>
# # RangeIndex: 10 entries, 0 to 9
# # Data columns (total 5 columns):
# #  #   Column        Non-Null Count  Dtype  
# # ---  ------        --------------  -----  
# #  0   Name          10 non-null     str    
# #  1   City          10 non-null     str    
# #  2   Marks         9 non-null      float64
# #  3   Age           10 non-null     int64  
# #  4   Joining_Date  10 non-null     str    
# # dtypes: float64(1), int64(1), str(3)

# #Missing values.
# print(df.isnull().sum())
# # Name            0
# # City            0
# # Marks           1
# # Age             0
# # Joining_Date    0
# # dtype: int64

# #Fill missing Marks with average.
# df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
# print(df)
# # 0    Aman   Delhi  85.000000   18   2026-01-10
# # 1   Rohit  Indore  90.000000   19   2026-02-15
# # 2    Neha   Delhi  78.000000   18   2026-03-20
# # 3   Priya  Bhopal  95.000000   20   2026-01-25
# # 4   Arjun  Indore  88.000000   19   2026-04-10
# # 5   Sneha   Delhi  86.222222   18   2026-05-12
# # 6   Karan  Bhopal  91.000000   20   2026-02-28
# # 7   Pooja  Indore  84.000000   19   2026-03-18
# # 8   Vivek   Delhi  76.000000   18   2026-01-05
# # 9  Anjali  Bhopal  89.000000   20   2026-06-01

# #Highest Marks.
# print(df["Marks"].max())
# # 95.0

# print(df.sort_values("Marks", ascending=False).head(1))
# #     Name    City  Marks  Age Joining_Date
# # 3  Priya  Bhopal   95.0   20   2026-01-25

 
# #Lowest Marks.
# print(df["Marks"].min())
# # 76.0

# print(df.sort_values("Marks").head(1))
# #     Name   City  Marks  Age Joining_Date
# # 8  Vivek  Delhi   76.0   18   2026-01-05

# #Average Marks.
# print(df["Marks"].mean())
# # 86.22222222222223

# #Students scoring above 85.
# print(df[df["Marks"] > 85])
# #      Name    City  Marks  Age Joining_Date
# # 1   Rohit  Indore   90.0   19   2026-02-15
# # 3   Priya  Bhopal   95.0   20   2026-01-25
# # 4   Arjun  Indore   88.0   19   2026-04-10
# # 6   Karan  Bhopal   91.0   20   2026-02-28
# # 9  Anjali  Bhopal   89.0   20   2026-06-01

# #Sort by Marks.
# print(df.sort_values("Marks", ascending=False))
# #      Name    City  Marks  Age Joining_Date
# # 3   Priya  Bhopal   95.0   20   2026-01-25
# # 6   Karan  Bhopal   91.0   20   2026-02-28
# # 1   Rohit  Indore   90.0   19   2026-02-15
# # 9  Anjali  Bhopal   89.0   20   2026-06-01
# # 4   Arjun  Indore   88.0   19   2026-04-10
# # 0    Aman   Delhi   85.0   18   2026-01-10
# # 7   Pooja  Indore   84.0   19   2026-03-18
# # 2    Neha   Delhi   78.0   18   2026-03-20
# # 8   Vivek   Delhi   76.0   18   2026-01-05
# # 5   Sneha   Delhi    NaN   18   2026-05-12

# print(df.sort_values("Marks"))
# #      Name    City  Marks  Age Joining_Date
# # 8   Vivek   Delhi   76.0   18   2026-01-05
# # 2    Neha   Delhi   78.0   18   2026-03-20
# # 7   Pooja  Indore   84.0   19   2026-03-18
# # 0    Aman   Delhi   85.0   18   2026-01-10
# # 4   Arjun  Indore   88.0   19   2026-04-10
# # 9  Anjali  Bhopal   89.0   20   2026-06-01
# # 1   Rohit  Indore   90.0   19   2026-02-15
# # 6   Karan  Bhopal   91.0   20   2026-02-28
# # 3   Priya  Bhopal   95.0   20   2026-01-25
# # 5   Sneha   Delhi    NaN   18   2026-05-12

# #Average marks city-wise.
# print(df.groupby("City")["Marks"].mean())
# # City
# # Bhopal    91.666667
# # Delhi     79.666667
# # Indore    87.333333
# # Name: Marks, dtype: float64

# #Convert Joining_Date.
# # df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])
# # df["Year"] = df["Joining_Date"].dt.year
# # df["Month"] = df["Joining_Date"].dt.month
# # df["Month_name"] = df["Joining_Date"].dt.month_name()
# # df["Day"] = df["Joining_Date"].dt.day
# # df["Day_name"] = df["Joining_Date"].dt.day_name()
# # df["Weekday"] = df["Joining_Date"].dt.weekday
# # print(df)

# #      Name    City  Marks  Age Joining_Date  Year  Month Month_name  Day   Day_name  Weekday
# # 0    Aman   Delhi   85.0   18   2026-01-10  2026      1    January   10   Saturday        5
# # 1   Rohit  Indore   90.0   19   2026-02-15  2026      2   February   15     Sunday        6
# # 2    Neha   Delhi   78.0   18   2026-03-20  2026      3      March   20     Friday        4
# # 3   Priya  Bhopal   95.0   20   2026-01-25  2026      1    January   25     Sunday        6
# # 4   Arjun  Indore   88.0   19   2026-04-10  2026      4      April   10     Friday        4
# # 5   Sneha   Delhi    NaN   18   2026-05-12  2026      5        May   12    Tuesday        1
# # 6   Karan  Bhopal   91.0   20   2026-02-28  2026      2   February   28   Saturday        5
# # 7   Pooja  Indore   84.0   19   2026-03-18  2026      3      March   18  Wednesday        2
# # 8   Vivek   Delhi   76.0   18   2026-01-05  2026      1    January    5     Monday        0
# # 9  Anjali  Bhopal   89.0   20   2026-06-01  2026      6       June    1     Monday        0

# #tudents joined after March.
# print(df[df["Joining_Date"] > "2026-03-20"])
# #      Name    City  Marks  Age Joining_Date
# # 4   Arjun  Indore   88.0   19   2026-04-10
# # 5   Sneha   Delhi    NaN   18   2026-05-12
# # 9  Anjali  Bhopal   89.0   20   2026-06-01


#Final Clean Data.
#     Name    City  Marks  Age Joining_Date
# 0   Aman   Delhi   85.0   18   2026-01-10
# 1  Rohit  Indore   90.0   19   2026-02-15
# 2   Neha   Delhi   78.0   18   2026-03-20
# 3  Priya  Bhopal   95.0   20   2026-01-25
# 4  Arjun  Indore   88.0   19   2026-04-10
# <class 'pandas.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 5 columns):
#  #   Column        Non-Null Count  Dtype  
# ---  ------        --------------  -----  
#  0   Name          10 non-null     str    
#  1   City          10 non-null     str    
#  2   Marks         9 non-null      float64
#  3   Age           10 non-null     int64  
#  4   Joining_Date  10 non-null     str    
# dtypes: float64(1), int64(1), str(3)
# memory usage: 532.0 bytes
# None
# Name            0
# City            0
# Marks           1
# Age             0
# Joining_Date    0
# dtype: int64
#      Name    City      Marks  Age Joining_Date
# 0    Aman   Delhi  85.000000   18   2026-01-10
# 1   Rohit  Indore  90.000000   19   2026-02-15
# 2    Neha   Delhi  78.000000   18   2026-03-20
# 3   Priya  Bhopal  95.000000   20   2026-01-25
# 4   Arjun  Indore  88.000000   19   2026-04-10
# 5   Sneha   Delhi  86.222222   18   2026-05-12
# 6   Karan  Bhopal  91.000000   20   2026-02-28
# 7   Pooja  Indore  84.000000   19   2026-03-18
# 8   Vivek   Delhi  76.000000   18   2026-01-05
# 9  Anjali  Bhopal  89.000000   20   2026-06-01
# 95.0
#     Name    City  Marks  Age Joining_Date
# 3  Priya  Bhopal   95.0   20   2026-01-25
# 76.0
#     Name   City  Marks  Age Joining_Date
# 8  Vivek  Delhi   76.0   18   2026-01-05
# 86.22222222222221
#      Name    City      Marks  Age Joining_Date
# 1   Rohit  Indore  90.000000   19   2026-02-15
# 3   Priya  Bhopal  95.000000   20   2026-01-25
# 4   Arjun  Indore  88.000000   19   2026-04-10
# 5   Sneha   Delhi  86.222222   18   2026-05-12
# 6   Karan  Bhopal  91.000000   20   2026-02-28
# 9  Anjali  Bhopal  89.000000   20   2026-06-01
#      Name    City      Marks  Age Joining_Date
# 3   Priya  Bhopal  95.000000   20   2026-01-25
# 6   Karan  Bhopal  91.000000   20   2026-02-28
# 1   Rohit  Indore  90.000000   19   2026-02-15
# 9  Anjali  Bhopal  89.000000   20   2026-06-01
# 4   Arjun  Indore  88.000000   19   2026-04-10
# 5   Sneha   Delhi  86.222222   18   2026-05-12
# 0    Aman   Delhi  85.000000   18   2026-01-10
# 7   Pooja  Indore  84.000000   19   2026-03-18
# 2    Neha   Delhi  78.000000   18   2026-03-20
# 8   Vivek   Delhi  76.000000   18   2026-01-05
#      Name    City      Marks  Age Joining_Date
# 8   Vivek   Delhi  76.000000   18   2026-01-05
# 2    Neha   Delhi  78.000000   18   2026-03-20
# 7   Pooja  Indore  84.000000   19   2026-03-18
# 0    Aman   Delhi  85.000000   18   2026-01-10
# 5   Sneha   Delhi  86.222222   18   2026-05-12
# 4   Arjun  Indore  88.000000   19   2026-04-10
# 9  Anjali  Bhopal  89.000000   20   2026-06-01
# 1   Rohit  Indore  90.000000   19   2026-02-15
# 6   Karan  Bhopal  91.000000   20   2026-02-28
# 3   Priya  Bhopal  95.000000   20   2026-01-25
# City
# Bhopal    91.666667
# Delhi     81.305556
# Indore    87.333333
# Name: Marks, dtype: float64
#      Name    City      Marks  Age Joining_Date
# 4   Arjun  Indore  88.000000   19   2026-04-10
# 5   Sneha   Delhi  86.222222   18   2026-05-12
# 9  Anjali  Bhopal  89.000000   20   2026-06-01

#bonus
# df["Result"] = df["Marks"].apply(
#     lambda x: "Pass" if x >= 40 else "Fail"
# )
# print(df)

# df["Time_"] = df["Joining_Date"].apply(
#     lambda x: "timetotime" if x <= "2026-05-12" else "Late"
# )
# print(df)
# 0    Aman   Delhi   85.0   18   2026-01-10  timetotime
# 1   Rohit  Indore   90.0   19   2026-02-15  timetotime
# 2    Neha   Delhi   78.0   18   2026-03-20  timetotime
# 3   Priya  Bhopal   95.0   20   2026-01-25  timetotime
# 4   Arjun  Indore   88.0   19   2026-04-10  timetotime
# 5   Sneha   Delhi    NaN   18   2026-05-12  timetotime
# 6   Karan  Bhopal   91.0   20   2026-02-28  timetotime
# 7   Pooja  Indore   84.0   19   2026-03-18  timetotime
# 8   Vivek   Delhi   76.0   18   2026-01-05  timetotime
# 9  Anjali  Bhopal   89.0   20   2026-06-01        Late

#⭐ Bonus 2 grade system

# def grade(x):
#     if x >= 90:
#         return "A+"
#     elif x >= 80:
#         return "A"
#     elif x >= 70:
#         return "B"
#     else:
#         return "C"

# df["Grade"] = df["Marks"].apply(grade)
# print(df)
# 0    Aman   Delhi   85.0   18   2026-01-10     A
# 1   Rohit  Indore   90.0   19   2026-02-15    A+
# 2    Neha   Delhi   78.0   18   2026-03-20     B
# 3   Priya  Bhopal   95.0   20   2026-01-25    A+
# 4   Arjun  Indore   88.0   19   2026-04-10     A
# 5   Sneha   Delhi    NaN   18   2026-05-12     C
# 6   Karan  Bhopal   91.0   20   2026-02-28    A+
# 7   Pooja  Indore   84.0   19   2026-03-18     A
# 8   Vivek   Delhi   76.0   18   2026-01-05     B
# 9  Anjali  Bhopal   89.0   20   2026-06-01     A

 