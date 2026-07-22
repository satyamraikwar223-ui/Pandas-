import pandas as pd

df = pd.DataFrame({
    "Day": [
        "Mon","Tue","Wed",
        "Thu","Fri","Sat","Sun"
    ],
    "Sales": [100,150,120,180,200,170,220]
})

#print(df)

# df["Running_Total"] = df["Sales"].cumsum()
# print(df)
# 0  Mon    100            100
# 1  Tue    150            250
# 2  Wed    120            370
# 3  Thu    180            550
# 4  Fri    200            750
# 5  Sat    170            920
# 6  Sun    220           1140

# df["Running_Max"] = df["Sales"].cummax()
# print(df)
#    Day  Sales  Running_Max
# 0  Mon    100          100
# 1  Tue    150          150
# 2  Wed    120          150
# 3  Thu    180          180
# 4  Fri    200          200
# 5  Sat    170          200
# 6  Sun    220          220

# df["Running_Min"] = df["Sales"].cummin()
# print(df)
#    Day  Sales  Running_Min
# 0  Mon    100          100
# 1  Tue    150          100
# 2  Wed    120          100
# 3  Thu    180          100
# 4  Fri    200          100
# 5  Sat    170          100
# 6  Sun    220          100

# df["Product"] = df["Sales"].cumprod()
# print(df)
#    Day  Sales           Product
# 0  Mon    100               100
# 1  Tue    150             15000
# 2  Wed    120           1800000
# 3  Thu    180         324000000
# 4  Fri    200       64800000000
# 5  Sat    170    11016000000000
# 6  Sun    220  2423520000000000

# df["Rolling_Avg"] = df["Sales"].rolling(3).mean()
# print(df)
#    Day  Sales  Rolling_Avg
# 0  Mon    100          NaN
# 1  Tue    150          NaN
# 2  Wed    120   123.333333
# 3  Thu    180   150.000000
# 4  Fri    200   166.666667
# 5  Sat    170   183.333333
# 6  Sun    220   196.666667

 
# df["Rolling_max"] = df["Sales"].rolling(3).max() also min()
# print(df)
#    Day  Sales  Rolling_max
# 0  Mon    100          NaN
# 1  Tue    150          NaN
# 2  Wed    120        150.0
# 3  Thu    180        180.0
# 4  Fri    200        200.0
# 5  Sat    170        200.0
# 6  Sun    220        220.0

# df["Expanding_Mean"] = df["Sales"].expanding().mean() also max() min()

# print(df)
#    Day  Sales  Expanding_Mean
# 0  Mon    100      100.000000
# 1  Tue    150      125.000000
# 2  Wed    120      123.333333
# 3  Thu    180      137.500000
# 4  Fri    200      150.000000
# 5  Sat    170      153.333333
# 6  Sun    220      162.857143