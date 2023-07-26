

#     ***************** one by one data get Excel in SQLLite Db *****************


# import pandas as pd 
# import sqlite3

# df = pd.read_excel('C:\Anjali\Kunti Tenders\Khunti_All_Page.xlsx')  ####   excel file path
# connection = sqlite3.connect('C:\Anjali\Kunti Tenders\khunti_db.db') ####  save database path

# df.to_sql(name = 'Khunti_All_Page', con = connection, if_exists= 'replace', index=False,
# dtype = {'Title': 'text', 'Description': 'text', 'Start Date': 'real', 'End Date': 'real', 'File': 'text', 'SourceUrl': 'text'})

# connection.commit()
# connection.close()



#     ***************** one by one data get csv in SQLLite Db *****************

                # df = pd.read_csv(file_Folder_Name + '.csv')
                # logging.info('Insert Data Into Database')
                # df.to_sql(name='Khunti_All_Page', con=connection, if_exists='replace', index=False, dtype={'Title': 'text', 'Description': 'text', 'Start Date': 'real', 'End Date': 'real', 'File': 'text', 'SourceUrl': 'text'})
                # print("----database  insertted-------------")
