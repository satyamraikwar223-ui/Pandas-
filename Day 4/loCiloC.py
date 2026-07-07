import pandas as pd 

students = { "name":["satyam", "shivam", "lakshya", "satya"],
             "age" :["18", "20", "18", "18"],
             "city" :["kjahuraho", "indore", "indore", "bhopal"],
             "fav_subject" :["maths", "science", "english", "hindi"]
}


df = pd.DataFrame(students)
print(df)

print(df.loc[0]) # it will print the first row of the data frame
#output:
# name              satyam
# age                   18
# city           kjahuraho
# fav_subject        maths
# Name: 0, dtype: str


print(df.iloc[0]) # it will also print the first row of the data frame
#output:
# name              satyam
# age                   18
# city           kjahuraho
# fav_subject        maths
# Name: 0, dtype: str

print(df.loc[0, "name"]) # it will print the name of the first row
#output:
# satyam

print(df.iloc[0, 0]) # it will also print the name of the first row
#output:
# satyam

print(df.loc[1:2])# it will print the second and third row of the data frame
#output:
#     name age    city fav_subject
# 1  shivam  20  indore     science
# 2  lakshya  18  indore     english

print(df.iloc[1:2])# it will also print the second row of the data frame
#output:
#     name age    city fav_subject
# 1  shivam  20  indore     science 

print(df.loc[1:2, "name"]) # it will print the name of the second and third row
#output:
# 1     shivam
# 2    lakshya

print(df.iloc[1:2, 0]) # it will also print the name of the second row
#output:
# 1    shivam

print(df.loc[:, ["name", "age"]]) # it will print the name and age of all the rows
#output:
#       name age
# 0    satyam  18
# 1    shivam  20
# 2   lakshya  18
# 3     satya  18

print(df.iloc[:, [0, 1]]) # it will also print the name and age of all the rows
#output:
#       name age
# 0    satyam  18
# 1    shivam  20

print(df.iloc[0:2, 0:2]) # it will print the name and age of the first and second row
#output:
#       name age
# 0    satyam  18
# 1    shivam  20



