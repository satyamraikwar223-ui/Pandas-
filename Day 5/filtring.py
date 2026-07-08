import pandas as pd

# Create DataFrame
employees = {
    "Emp_ID": [101,102,103,104,105,106,107,108,109,110,
               111,112,113,114,115,116,117,118,119,120],

    "Name": ["Aman","Rohit","Priya","Neha","Karan",
             "Anjali","Vikas","Sneha","Rahul","Pooja",
             "Riya","Arjun","Kavita","Mohit","Simran",
             "Deepak","Nisha","Yash","Meena","Ajay"],

    "Age": [22,25,28,24,30,27,35,29,26,23,
            31,32,27,24,29,34,26,28,33,25],

    "Department": ["HR","IT","Finance","IT","HR",
                   "Sales","Finance","IT","Sales","HR",
                   "Marketing","Finance","IT","Sales","HR",
                   "Marketing","Finance","IT","Sales","HR"],

    "City": ["Bhopal","Indore","Gwalior","Jabalpur","Sagar",
             "Bhopal","Indore","Gwalior","Jabalpur","Sagar",
             "Bhopal","Indore","Gwalior","Jabalpur","Sagar",
             "Bhopal","Indore","Gwalior","Jabalpur","Sagar"],

    "Salary": [30000,45000,50000,42000,55000,
               38000,62000,47000,41000,35000,
               65000,70000,48000,39000,52000,
               68000,60000,46000,43000,36000]
}

df = pd.DataFrame(employees)

#print(df)

#print(df[df['Age'] > 30])  # Filter employees older than 30
#output:
# Emp_ID    Name  Age Department      City  Salary
# 6      107   Vikas   35    Finance    Indore   62000
# 10     111    Riya   31  Marketing    Bhopal   65000
# 11     112   Arjun   32    Finance    Indore   70000
# 15     116  Deepak   34  Marketing    Bhopal   68000
# 18     119   Meena   33      Sales  Jabalpur   43000

#print(df[df["Age"] == 30])  # Filter employees who are exactly 30 years old
#output:
# Emp_ID   Name  Age Department   City  Salary
# 4      105  Karan   30        HR  Sagar

#print(df[df["Department"] == "IT"])  # Filter employees in the IT department
#output:

#     Emp_ID    Name  Age Department      City  Salary
# 1      102   Rohit   25         IT    Indore   45000
# 3      104    Neha   24         IT  Jabalpur   42000
# 7      108   Sneha   29         IT   Gwalior   47000
# 12     113  Kavita   27         IT   Gwalior   48000
# 17     118    Yash   28         IT   Gwalior   46000

#print(df[df["Salary"] != 50000]) # Filter employees whose salary is not equal to 50000
#output:
#     Emp_ID    Name  Age Department      City  Salary
# 0      101    Aman   22         HR    Bhopal   30000
# 1      102   Rohit   25         IT    Indore   45000
# 3      104    Neha   24         IT  Jabalpur   42000
# 4      105   Karan   30         HR     Sagar   55000
# 5      106  Anjali   27      Sales    Bhopal   38000
# 6      107   Vikas   35    Finance    Indore   62000
# 7      108   Sneha   29         IT   Gwalior   47000
# 8      109   Rahul   26      Sales  Jabalpur   41000
# 9      110   Pooja   23         HR     Sagar   35000
# 10     111    Riya   31  Marketing    Bhopal   65000
# 11     112   Arjun   32    Finance    Indore   70000
# 12     113  Kavita   27         IT   Gwalior   48000
# 13     114   Mohit   24      Sales  Jabalpur   39000
# 14     115  Simran   29         HR     Sagar   52000
# 15     116  Deepak   34  Marketing    Bhopal   68000
# 16     117   Nisha   26    Finance    Indore   60000
# 17     118    Yash   28         IT   Gwalior   46000
# 18     119   Meena   33      Sales  Jabalpur   43000
# 19     120    Ajay   25         HR     Sagar   36000

#print(df[df["City"].isin(["Bhopal", "Indore"])])  # Filter employees in Bhopal or Indore
#output:
#Emp_ID    Name  Age Department    City  Salary
# 0      101    Aman   22         HR  Bhopal   30000
# 1      102   Rohit   25         IT  Indore   45000
# 5      106  Anjali   27      Sales  Bhopal   38000
# 6      107   Vikas   35    Finance  Indore   62000
# 10     111    Riya   31  Marketing  Bhopal   65000
# 11     112   Arjun   32    Finance  Indore   70000
# 15     116  Deepak   34  Marketing  Bhopal   68000
# 16     117   Nisha   26    Finance  Indore   60000

#print(df[df["Salary"].between(40000, 60000)])  # Filter employees with salary between 40000 and 60000
#output:
#       Emp_ID  Name  Age    Department  City    Salary
# 1      102   Rohit   25         IT    Indore   45000
# 2      103   Priya   28    Finance   Gwalior   50000
# 3      104    Neha   24         IT  Jabalpur   42000
# 4      105   Karan   30         HR     Sagar   55000
# 7      108   Sneha   29         IT   Gwalior   47000
# 8      109   Rahul   26      Sales  Jabalpur   41000
# 12     113  Kavita   27         IT   Gwalior   48000
# 14     115  Simran   29         HR     Sagar   52000
# 16     117   Nisha   26    Finance    Indore   60000
# 17     118    Yash   28         IT   Gwalior   46000
# 18     119   Meena   33      Sales  Jabalpur   43000

#print(df[df["Age"].between(25, 30) & df["Department"].isin(["IT", "Finance"])])  # Filter employees aged between 25 and 30 in IT or Finance departments 
#output:
#     Emp_ID    Name  Age Department     City  Salary
# 1      102   Rohit   25         IT   Indore   45000
# 2      103   Priya   28    Finance  Gwalior   50000
# 7      108   Sneha   29         IT  Gwalior   47000
# 12     113  Kavita   27         IT  Gwalior   48000
# 16     117   Nisha   26    Finance   Indore   60000
# 17     118    Yash   28         IT  Gwalior   46000

#print(df[(df["City"] == "Bhopal") | (df["City"] == "Indore")]) # Filter employees in Bhopal or Indore
#output:
#     Emp_ID    Name  Age Department    City  Salary
# 0      101    Aman   22         HR  Bhopal   30000
# 1      102   Rohit   25         IT  Indore   45000
# 5      106  Anjali   27      Sales  Bhopal   38000
# 6      107   Vikas   35    Finance  Indore   62000
# 10     111    Riya   31  Marketing  Bhopal   65000
# 11     112   Arjun   32    Finance  Indore   70000
# 15     116  Deepak   34  Marketing  Bhopal   68000
# 16     117   Nisha   26    Finance  Indore   60000

#print(df[(df["Age"] > 25) & (df["City"] == "Indore")])  # Filter employees older than 25 and in Indore
#output:
#     Emp_ID   Name  Age Department    City  Salary
# 6      107  Vikas   35    Finance  Indore   62000
# 11     112  Arjun   32    Finance  Indore   70000
# 16     117  Nisha   26    Finance  Indore   60000

#print(df[df["Age"] == 25]["Name"]) # Filter employees who are exactly 25 years old and display their names
#output:
# 1     Rohit
# 19     Ajay
# Name: Name, dtype: str



