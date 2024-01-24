import pandas as pd

df = pd.read_csv('df.csv')
dfloan = pd.read_csv('2023_loan.csv')


df["first_name"] = df["first_name"].str.upper() 
df["last_name"] = df["last_name"].str.upper() 
df["last_name"] = df["last_name"].str.strip() 
df["first_name"] = df["first_name"].str.strip() 
merged_df = pd.merge(df, dfloan, on=['first_name', 'last_name'], how='inner')

# dfloan["last_name"] = dfloan["last_name"].str.lower() 
# dfloan["first_name"] = dfloan["first_name"].str.lower() 

print(merged_df)