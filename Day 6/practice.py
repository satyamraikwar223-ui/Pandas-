import pandas as pd
employee = {
    "Name": ["Aman", "Rohit", "Neha", "Priya", "Arjun", "Karan"],
    "Department": ["HR", "IT", "HR", "Finance", "IT", "Finance"],
    "Salary": [30000, 55000, 35000, 60000, 52000, 45000],
    "Experience": [2, 5, 3, 6, 4, 2]
}

df = pd.DataFrame(employee)

# Question: Display the top 2 highest paid employees in the IT department.
print(df[df["Department"] == "IT"].sort_values("Salary", ascending=False).head(2))
# output:
#    Name Department  Salary  Experience
# 1  Rohit         IT   55000           5
# 4  Arjun         IT   52000           4