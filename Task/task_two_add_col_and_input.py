
import pandas as pd

df = pd.read_csv("test.csv")  ### read csv file

title_col = int(input("Enter Number: "))  ### input in title match
name_col = input("Enter Name: ")   ### second col input

df.loc[title_col, 'Name'] = name_col  ### title input and col name 
print(df)

df.to_csv("test.csv", index=False) ###  write object to comma 
