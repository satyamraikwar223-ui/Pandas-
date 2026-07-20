import pandas as pd

df = pd.DataFrame({
    "City": [
        "Delhi","Delhi","Indore",
        "Indore","Delhi","Bhopal"
    ],
    "Product": [
        "Laptop","Mobile","Laptop",
        "Mobile","Laptop","Laptop"
    ],
    "Sales": [
        50000,30000,45000,
        25000,55000,47000
    ]
})

#print(df)

# print(df.groupby(["City", "Product"])["Sales"].sum())

# City    Product
# Bhopal  Laptop      47000
# Delhi   Laptop     105000
#         Mobile      30000
# Indore  Laptop      45000
#         Mobile      25000
# Name: Sales, dtype: int64

# print(df.groupby(["City", "Product"])["Sales"].agg(["sum", "mean", "min", "max", "count", "size"]))

#                    sum     mean    min    max  count  size
# City   Product                                            
# Bhopal Laptop    47000  47000.0  47000  47000      1     1
# Delhi  Laptop   105000  52500.0  50000  55000      2     2
#        Mobile    30000  30000.0  30000  30000      1     1
# Indore Laptop    45000  45000.0  45000  45000      1     1
#        Mobile    25000  25000.0  25000  25000      1     1

# print(df.groupby(["City", "Product"])["Sales"].agg(["sum", "mean", "min", "max", "count", "size"]).reset_index())

#      City Product     sum     mean    min    max  count  size
# 0  Bhopal  Laptop   47000  47000.0  47000  47000      1     1
# 1   Delhi  Laptop  105000  52500.0  50000  55000      2     2
# 2   Delhi  Mobile   30000  30000.0  30000  30000      1     1
# 3  Indore  Laptop   45000  45000.0  45000  45000      1     1
# 4  Indore  Mobile   25000  25000.0  25000  25000      1     1


# print(df.groupby(["City", "Product"])
#       .filter(
#          lambda x:
#          x["Sales"].agg(["sum", "mean", "min", "max", "count", "size"]) > 45000))


# print(
#     df.groupby("City")
#       .filter(
#           lambda x:
#           x["Sales"].mean() > 40000
#       )
# )

#      City Product  Sales
# 0   Delhi  Laptop  50000
# 1   Delhi  Mobile  30000
# 4   Delhi  Laptop  55000
# 5  Bhopal  Laptop  47000