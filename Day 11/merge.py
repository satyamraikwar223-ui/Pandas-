import pandas as pd

employees = pd.DataFrame({
    "Emp_ID": [1, 2, 3, 4],
    "Name": ["Aman", "Rohit", "Neha", "Priya"]
})

salary = pd.DataFrame({
    "Emp_ID": [1, 2, 4, 5],
    "Salary": [30000, 55000, 60000, 45000]
})

# result = pd.merge(employees, salary, on="Emp_ID")
# print(result)
# output:
#    Emp_ID   Name  Salary
# 0       1   Aman   30000
# 1       2  Rohit   55000
# 2       4  Priya   60000

# result = pd.merge(employees, salary, on="Emp_ID", how="left")
# print(result)
# output:
#    Emp_ID   Name   Salary
# 0       1   Aman  30000.0
# 1       2  Rohit  55000.0
# 2       3   Neha      NaN
# 3       4  Priya  60000.0

#result = pd.merge(employees, salary, on="Emp_ID", how="right")
#print(result)
# output:
#    Emp_ID   Name  Salary
# 0       1   Aman   30000
# 1       2  Rohit   55000
# 2       4  Priya   60000
# 3       5    NaN   45000

#result = pd.merge(employees, salary, on="Emp_ID", how="outer")
#print(result)
# output:
#    Emp_ID   Name   Salary
# 0       1   Aman  30000.0
# 1       2  Rohit  55000.0
# 2       3   Neha      NaN
# 3       4  Priya  60000.0
# 4       5    NaN  45000.0

# result = employees.join(salary)

# result = pd.merge(employees, salary, on="Emp_ID", how="outer", indicator=True)
# print(result)
# output:
#    Emp_ID   Name   Salary      _merge
# 0       1   Aman  30000.0        both
# 1       2  Rohit  55000.0        both
# 2       3   Neha      NaN   left_only
# 3       4  Priya  60000.0        both
# 4       5    NaN  45000.0  right_only












