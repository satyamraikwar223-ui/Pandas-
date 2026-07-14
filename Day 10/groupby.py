import pandas as pd

employee = {
    "Name": ["Aman", "Rohit", "Neha", "Priya", "Arjun", "Karan"],
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance"],
    "Salary": [30000, 55000, 35000, 60000, 52000, 45000],
    "Experience": [2, 5, 3, 6, 4, 2]
}

df = pd.DataFrame(employee)

# print(df.groupby("Name"))
# output:
# <pandas.api.typing.DataFrameGroupBy object at 0x0000014C179F98D0>
 
# print(df.groupby("Department")["Salary"].sum())
# output:
# Department
# Finance    105000
# HR          65000
# IT         107000
# Name: Salary, dtype: int64

# print(df.groupby("Department")["Salary"].mean())
# output:
# Department
# Finance    52500.0
# HR         32500.0
# IT         53500.0
# Name: Salary, dtype: float64

# print(df.groupby("Department")["Name"].count())
# output:
# Department
# Finance    2
# HR         2
# IT         2
# Name: Name, dtype: int64

# print(df.groupby("Department")["Salary"].max())
# output:
# Department
# Finance    60000
# HR         35000
# IT         55000
# Name: Salary, dtype: int64

# print(df.groupby("Department")["Salary"].min())
# output:
# Department
# Finance    45000
# HR         30000
# IT         52000
# Name: Salary, dtype: int64

# print(df.groupby("Department")["Salary"].agg(["max" , "min" , "sum" , "count" , "mean"]))
# output:
#               max    min     sum  count     mean
# Department                                      
# Finance     60000  45000  105000      2  52500.0
# HR          35000  30000   65000      2  32500.0
# IT          55000  52000  107000      2  53500.0

# print(df.groupby(["Name" , "Department" , "Experience"])["Salary"].agg(["max" , "min" , "sum" , "count" , "mean"]))
# output:
#                                max    min    sum  count     mean
# Name  Department Experience                                     
# Aman  HR         2           30000  30000  30000      1  30000.0
# Arjun IT         4           52000  52000  52000      1  52000.0
# Karan Finance    2           45000  45000  45000      1  45000.0
# Neha  HR         3           35000  35000  35000      1  35000.0
# Priya Finance    6           60000  60000  60000      1  60000.0
# Rohit IT         5           55000  55000  55000      1  55000.0

# print(df.groupby("Department").size())
# output:
# Department
# Finance    2
# HR         2
# IT         2
# dtype: int64

# print(df.groupby("Experience").size())
# output:
# Experience
# 2    2
# 3    1
# 4    1
# 5    1
# 6    1
# dtype: int64

