import pandas as pd

employee = pd.DataFrame({
    "Name": ["Aman", "Rohit", "Neha", "Priya"],
    "Department": ["IT", "HR", "Finance", "IT"],
    "Salary": [60000, 40000, 70000, 65000]
})

# dept_code = {
#     "IT": "I01",
#     "HR": "H01",
#     "Finance": "F01"
# }
# employee["Dept_Code"] = employee["Department"].map(dept_code)
# print(employee)
#     Name Department  Salary Dept_Code
# 0   Aman         IT   60000       I01
# 1  Rohit         HR   40000       H01
# 2   Neha    Finance   70000       F01
# 3  Priya         IT   65000       I01

# employee["About_Exp"] = employee["Salary"].apply(
#     lambda x: "Experienced" if x > 60000 else "Non-Experienced"
# )
# print(employee)
#     Name Department  Salary        About_Exp
# 0   Aman         IT   60000  Non-Experienced
# 1  Rohit         HR   40000  Non-Experienced
# 2   Neha    Finance   70000      Experienced
# 3  Priya         IT   65000      Experienced

# def exp(x):
#     if x >  60000:
#         return "Senior" 
#     elif x == 60000:
#         return "Midexp"
#     else:
#         return "Junior"
# employee["Value_Place"] = employee["Salary"].apply(exp)
    
# print(employee)

#     Name Department  Salary Value_Place
# 0   Aman         IT   60000      Midexp
# 1  Rohit         HR   40000      Junior
# 2   Neha    Finance   70000      Senior
# 3  Priya         IT   65000      Senior

# employee["Total_Salary"] = employee["Salary"].apply(
#     lambda x: x + 5000
# )
# print(employee)
#     Name Department  Salary  Total_Salary
# 0   Aman         IT   60000         65000
# 1  Rohit         HR   40000         45000
# 2   Neha    Finance   70000         75000
# 3  Priya         IT   65000         70000

# employee["Name_Length"] = employee["Name"].apply(len)
# print(employee)
#     Name Department  Salary  Name_Length
# 0   Aman         IT   60000            4
# 1  Rohit         HR   40000            5
# 2   Neha    Finance   70000            4
# 3  Priya         IT   65000            5

# employee["Upper_Name"] = employee["Name"].apply(
#     lambda x: x.upper()
# )

# print(employee)
#     Name Department  Salary Upper_Name
# 0   Aman         IT   60000       AMAN
# 1  Rohit         HR   40000      ROHIT
# 2   Neha    Finance   70000       NEHA
# 3  Priya         IT   65000      PRIYA

# employee["Bonus"] = employee["Salary"].apply(
#     lambda x: x * 0.10
# )
# print(employee)
#     Name Department  Salary   Bonus
# 0   Aman         IT   60000  6000.0
# 1  Rohit         HR   40000  4000.0
# 2   Neha    Finance   70000  7000.0
# 3  Priya         IT   65000  6500.0