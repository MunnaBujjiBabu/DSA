import pandas as pd

data = {"name": ["Alice","Bob","Charlie"],"age": [25, 30, 35]}
df = pd.DataFrame(data)

# #display data frame
# print(df)

# #Accessing specific columns
# print(df["name"])


#Filtering rows based on a condition
print(df[df["age"]>30])