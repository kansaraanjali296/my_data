import pandas as pd
import pyodbc

conn = sql_conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=192.168.100.153;'
                                  'Database=CrawlingDB;'
                                  'UID=anjali;'
                                  'PWD=anjali@123;')

sql_query = pd.read_sql_query(''' 
                              select * from dbo.www_sbi_co_inpy_TenderListing
                              ''',conn)

df = pd.DataFrame(sql_query)
df.to_csv (r'C:\Users\kansara.anjali\Desktop\Python\www_sbi_co_in.csv', index = False)