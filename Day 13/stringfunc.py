import pandas as pd

df = pd.DataFrame({
    "Name": [" aman ", "ROHIT", "neha", "PRIYA"],
    "Department": ["hr", "IT", "finance", "HR"]
})


# print(df["Name"].str.upper())
# output:
# 0     AMAN 
# 1     ROHIT
# 2      NEHA
# 3     PRIYA
# Name: Name, dtype: str

#print(df["Name"].str.lower())
# output:
# 0     aman 
# 1     rohit
# 2      neha
# 3     priya
# Name: Name, dtype: str

# print(df["Name"].str.title())
# output:
# 0     Aman 
# 1     Rohit
# 2      Neha
# 3     Priya
# Name: Name, dtype: str

# print(df["Name"].str.startswith("R"))
#  output:
# 0    False
# 1     True
# 2    False
# 3    False
# Name: Name, dtype: bool

# print(df["Name"].str.endswith("A"))
#  output:
# 0    False
# 1    False
# 2    False
# 3     True
# Name: Name, dtype: bool

# print(df["Name"].str.strip()) #removes spaces
#   output:
# 0     aman
# 1    ROHIT
# 2     neha
# 3    PRIYA
# Name: Name, dtype: str

# print(df["Name"].str.replace("aman", "Satyam"))
# output:
# 0     Satyam 
# 1       ROHIT
# 2        neha
# 3       PRIYA
# Name: Name, dtype: str

#print(df["Name"].str.len())
#  output:

# 0    6
# 1    5
# 2    4
# 3    5
# Name: Name, dtype: int64


# df["Department"] = df["Department"].str.strip().str.title()

# print(df)
# output:
#      Name Department
# 0   aman          Hr
# 1   ROHIT         It
# 2    neha    Finance
# 3   PRIYA         Hr

# print(df[df["Department"].str.contains("fi", case=False)])
# output:
#    Name Department
# 2  neha    finance