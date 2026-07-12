import pandas as pd

employee = {
    "Name": ["Aman", "Rohit", "Aman", "Neha", "Priya", "Neha"],
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance"],
    "Salary": [30000, 55000, 30000, 60000, 52000, 60000]
}

df = pd.DataFrame(employee)
 
# print(df.duplicated()) #print true at the place of duplicated data
# output:
# 0    False
# 1    False
# 2     True
# 3    False
# 4    False
# 5     True
# dtype: bool

# print(df[df.duplicated()]) #prints duplicated data
# output:
#    Name Department  Salary
# 2  Aman         HR   30000
# 5  Neha    Finance   60000

# print(df.drop_duplicates()) #remove second duplicate value
# output:
#     Name Department  Salary
# 0   Aman         HR   30000
# 1  Rohit         IT   55000
# 3   Neha    Finance   60000
# 4  Priya         IT   52000

# df = df.drop_duplicates() #prints orignal dataframe without duplicate data
# print(df)
# output:
#     Name Department  Salary
# 0   Aman         HR   30000
# 1  Rohit         IT   55000
# 3   Neha    Finance   60000
# 4  Priya         IT   52000

# print(df.duplicated(subset=["Name"])) #prints true on the basis of duplicate name 
# output:
# 0    False
# 1    False
# 2     True
# 3    False
# 4    False
# 5     True
# dtype: bool
# 
# 
# print(df.duplicated(subset=["Salary" , "Name"]))
# output:
# 0    False
# 1    False
# 2     True
# 3    False
# 4    False
# 5     True
# dtype: bool

# print(df.drop_duplicates(keep="last")) #remove first duplicate value
# output:
#     Name Department  Salary
# 1  Rohit         IT   55000
# 2   Aman         HR   30000
# 4  Priya         IT   52000
# 5   Neha    Finance   60000

# print(df.drop_duplicates(keep=False)) # removes all record of duplicate data 
# output:
#     Name Department  Salary
# 1  Rohit         IT   55000
# 4  Priya         IT   52000

#total duplicate rows
# print(df.duplicated().sum())
# output:
# 2

print(df.duplicates())