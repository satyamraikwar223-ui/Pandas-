import pandas as pd

details = {
    "Name": ["satyam", "shivam", "lakshya"],
    "Age": [18, 20, 18],
    "City": ["khajuraho", "indore", "maharashtra"],
    "favfruit": ["mango", "banana", "apple"]
}
df = pd.DataFrame(details)


#print(df)
#output:     
#       Name  Age         City favfruit
# 0   satyam   18    khajuraho    mango
# 1   shivam   20       indore   banana
# 2  lakshya   18  maharashtra    apple

# print(df["Name"])
# output: 
# 0     satyam
# 1     shivam
# 2    lakshya
# Name: Name, dtype: str

# print(df.head(2))
# output: 
#      Name  Age       City favfruit
# 0  satyam   18  khajuraho    mango
# 1  shivam   20     indore   banana

# print(df.shape)
# output: (3, 4)

# print(df.tail(2))
# output: 
#      Name  Age         City favfruit
# 1  shivam   20       indore   banana
# 2  lakshya   18  maharashtra    apple

# print(df.describe())
# output:
#              Age
# count   3.000000
# mean   18.666667
# std     1.154701
# min    18.000000
# 25%    18.000000
# 50%    18.000000
# 75%    19.000000
# max    20.000000

# print(df.info())
# output:
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Name      3 non-null      str  
#  1   Age       3 non-null      int64
#  2   City      3 non-null      str  
#  3   favfruit  3 non-null      str  
# dtypes: int64(1), str(3)
# memory usage: 228.0 bytes
# None

