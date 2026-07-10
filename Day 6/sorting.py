import pandas as pd

employee = {
    "Name": ["Aman", "Rohit", "Neha", "Priya", "Arjun", "Karan"],
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance"],
    "Salary": [30000, 55000, 35000, 60000, 52000, 45000],
    "Experience": [2, 5, 3, 6, 4, 2]
}

df = pd.DataFrame(employee)

# print(df.sort_values("Name"))
# output:
#     Name Department  Salary  Experience
# 0   Aman         HR   30000           2
# 4  Arjun         IT   52000           4
# 5  Karan    Finance   45000           2
# 2   Neha         HR   35000           3
# 3  Priya    Finance   60000           6
# 1  Rohit         IT   55000           5

#print(df.sort_values("Name", ascending=False))
# output:
# 0    Name Department  Salary  Experience
# 1  Rohit         IT   55000           5
# 3  Priya    Finance   60000           6
# 2   Neha         HR   35000           3
# 5  Karan    Finance   45000           2
# 4  Arjun         IT   52000           4
# 0   Aman         HR   30000           2   

# print(df.sort_values(["Department", "Salary"], ascending=[True, False]))
# output:
#     Name Department  Salary  Experience
# 3  Priya    Finance   60000           6
# 5  Karan    Finance   45000           2
# 2   Neha         HR   35000           3
# 0   Aman         HR   30000           2
# 1  Rohit         IT   55000           5
# 4  Arjun         IT   52000           4

# print(df.sort_values("Salary", ascending=False).head(3))
# output:
#     Name Department  Salary  Experience
# 3  Priya    Finance   60000           6
# 1  Rohit         IT   55000           5
# 4  Arjun         IT   52000           4

# print(df.sort_values("Experience").tail(2))
# output:
#     Name Department  Salary  Experience
# 1  Rohit         IT   55000           5
# 3  Priya    Finance   60000           6

# print(df.sort_values("Salary", ascending=False).head(3).sort_values("Experience"))
# output:
#     Name Department  Salary  Experience
# 4  Arjun         IT   52000           4
# 1  Rohit         IT   55000           5
# 3  Priya    Finance   60000           6

# print(df.sort_values("Salary", ascending=False).head(3).sort_values("Experience", ascending=False))
# output:
#     Name Department  Salary  Experience
# 3  Priya    Finance   60000           6
# 1  Rohit         IT   55000           5
# 4  Arjun         IT   52000           4

# print(df.sort_index())
# output:
#     Name Department  Salary  Experience
# 0   Aman         HR   30000           2
# 1  Rohit         IT   55000           5
# 2   Neha         HR   35000           3
# 3  Priya    Finance   60000           6
# 4  Arjun         IT   52000           4
# 5  Karan    Finance   45000           2

# print(df.sort_index(ascending=False))
# output:
#     Name Department  Salary  Experience
# 5  Karan    Finance   45000           2
# 4  Arjun         IT   52000           4
# 3  Priya    Finance   60000           6
# 2   Neha         HR   35000           3
# 1  Rohit         IT   55000           5
# 0   Aman         HR   30000           2