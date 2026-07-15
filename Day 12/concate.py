import pandas as pd

morning = pd.DataFrame({
    "Student": ["Aman", "Rohit"],
    "Marks": [80, 90]
})

evening = pd.DataFrame({
    "Student": ["Neha", "Priya"],
    "Marks": [85, 95]
})

# print(pd.concat([morning, evening], keys=["Morning", "Evening"]))
# output:
#           Student  Marks
# Morning 0    Aman     80
#         1   Rohit     90
# Evening 0    Neha     85
#         1   Priya     95


# print(pd.concat([morning, evening]))
# output:
#   Student  Marks
# 0    Aman     80
# 1   Rohit     90
# 0    Neha     85
# 1   Priya     95

#print(pd.concat([morning, evening], ignore_index=True))
# output:
#   Student  Marks
# 0    Aman     80
# 1   Rohit     90
# 2    Neha     85
# 3   Priya     95

student = pd.DataFrame({
    "Name": ["Aman", "Rohit"]
})

age = pd.DataFrame({
    "Age": [20, 21]
})

# print(pd.concat([student, age], axis=1))
# output:
#     Name  Age
# 0   Aman   20
# 1  Rohit   21

#print(pd.concat([student, age], axis=0 , ignore_index=True))
# output:
#     Name   Age
# 0   Aman   NaN
# 1  Rohit   NaN
# 2    NaN  20.0
# 3    NaN  21.0

print(pd.concat([morning, evening], verify_integrity=True)) #Agar duplicate index honge to error dega.



