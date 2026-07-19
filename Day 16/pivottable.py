import pandas as pd

df = pd.DataFrame({
    "City": [
        "Delhi","Delhi",
        "Indore","Indore",
        "Bhopal","Bhopal",
        "Khajuraho"
    
    ],
    "Category": [
        "Mobile","Laptop",
        "Mobile","Laptop",
        "Mobile","Laptop",
        "NaN"
    ],
    "Amount": [
        30000,50000,
        25000,45000,
        28000,47000,
        50000
    ]
})
#👉 Default function = mean()
# print(pd.pivot_table(
#     df,
#     values="Amount",
#     index="City"
# ))

# Output:
# City
# Bhopal    37500.0
# Delhi     40000.0
# Indore    35000.0
# Name: Amount, dtype: float64
	

# print(df.groupby("City")["Amount"].mean())
# output:
# City
# Bhopal    37500.0
# Delhi     40000.0
# Indore    35000.0
# Name: Amount, dtype: float64

#2️⃣ Product-wise Pivot
# print(pd.pivot_table(
#     df,
#     values="Amount",
#     index="City",
#     columns="Category"
# ))

# Output:
# Category   Laptop   Mobile
# City                      
# Bhopal    47000.0  28000.0
# Delhi     50000.0  30000.0
# Indore    45000.0  25000.0

#3️⃣ Sum Instead of Mean
# print(pd.pivot_table(
#      df,
#     values="Amount",
#     index="City",
#     columns="Category",
#     aggfunc=["sum", "mean", "min", "max", "count"]
# ))
# output:
#             sum            mean             min           max         count       
# Category Laptop Mobile   Laptop   Mobile Laptop Mobile Laptop Mobile Laptop Mobile
# City                                                                              
# Bhopal    47000  28000  47000.0  28000.0  47000  28000  47000  28000      1      1
# Delhi     50000  30000  50000.0  30000.0  50000  30000  50000  30000      1      1
# Indore    45000  25000  45000.0  25000.0  45000  25000  45000  25000      1      1

#margin
# print(pd.pivot_table(
#     df,
#     values="Amount",
#     index="City",
#     columns="Category",
#     aggfunc="sum",
#     margins=True 

# ))
# output:
# Category  Laptop  Mobile     All
# City                            
# Bhopal     47000   28000   75000
# Delhi      50000   30000   80000
# Indore     45000   25000   70000
# All       142000   83000  225000

#6️⃣ Fill Missing Values
# print(pd.pivot_table(
#     df,
#     values="Amount",
#     index="City",
#     columns="Category",
#     fill_value=0
# ))
# OUTPUT:
# Category    Laptop   Mobile      NaN
# City                                
# Bhopal     47000.0  28000.0      0.0
# Delhi      50000.0  30000.0      0.0
# Indore     45000.0  25000.0      0.0
# Khajuraho      0.0      0.0  50000.0
