import pyodbc 
cnxn = pyodbc.connect('Driver={SQL Server};'
                        'Server=192.168.100.153;'
                        'Database=CrawlingDB;'
                        'UID=anjali;'
                        'PWD=anjali@123;')

cursor = cnxn.cursor()
cursor.execute("""IF NOT EXISTS (SELECT name FROM sysobjects WHERE name='khunti_nic_in' AND xtype='U') CREATE TABLE khunti_nic_in (id int IDENTITY(1,1) PRIMARY KEY, 
                                                                                                                                    Tender_Notice_No TEXT,                                                                                                                                
                                                                                                                                    Tender_Summery TEXT,
                                                                                                                                    Tender_Details TEXT,
                                                                                                                                    Bid_deadline_2 TEXT,
                                                                                                                                    Documents_2 TEXT,
                                                                                                                                    TenderListing_key TEXT,
                                                                                                                                    Notice_Type TEXT,
                                                                                                                                    Competition TEXT,
                                                                                                                                    Purchaser_Name TEXT,
                                                                                                                                    Pur_Add TEXT,
                                                                                                                                    Pur_State TEXT,
                                                                                                                                    Pur_City TEXT,
                                                                                                                                    Pur_Country TEXT,
                                                                                                                                    Pur_Email TEXT,
                                                                                                                                    Pur_URL TEXT,
                                                                                                                                    Bid_Deadline_1 TEXT,
                                                                                                                                    Financier_Name TEXT,
                                                                                                                                    CPV TEXT,
                                                                                                                                    scannedImage TEXT,
                                                                                                                                    Documents_1 TEXT,
                                                                                                                                    Documents_3 TEXT,
                                                                                                                                    Documents_4 TEXT,
                                                                                                                                    Documents_5 TEXT,
                                                                                                                                    currency TEXT,
                                                                                                                                    actualvalue TEXT,
                                                                                                                                    TenderFor TEXT,
                                                                                                                                    TenderType TEXT,
                                                                                                                                    SiteName TEXT,
                                                                                                                                    createdOn TEXT,
                                                                                                                                    updateOn TEXT,
                                                                                                                                    Content TEXT,
                                                                                                                                    Content1 TEXT,
                                                                                                                                    Content2 TEXT,
                                                                                                                                    Content3 TEXT,
                                                                                                                                    DocFees TEXT,
                                                                                                                                    EMD TEXT,
                                                                                                                                    OpeningDate TEXT,
                                                                                                                                    Tender_No TEXT)""") 
                                                                                                                                                                                                                                                            
cursor.execute("""INSERT INTO khunti_nic_in(Tender_Summery, Tender_Details) VALUES ('Desktop Computer', 'gg'),
                                                                                            ('Laptop', 'dd'), 
                                                                                            ('Tablet', 'rgvdfg'), 
                                                                                            ('Monitor', 'cfds'), 
                                                                                            ('Printer', 'sdfv'),
                                                                                            ('av', 'a')""")
                                                                                                                                                                
cnxn.commit()
cnxn.close()


# def create_msss(file_name):

#     import pyodbc 
#     cnxn = pyodbc.connect('Driver={SQL Server};'
#                             'Server=192.168.100.153;'
#                             'Database=CrawlingDB;'
#                             'UID=anjali;'
#                             'PWD=anjali@123;')

#     cursor = cnxn.cursor()
#     cursor.execute("IF NOT EXISTS (SELECT name FROM sysobjects WHERE name=" + file_name + "AND xtype='U') CREATE TABLE" + file_name +"""(id int IDENTITY(1,1) PRIMARY KEY, 
#                                                                                                                                         Tender_Notice_No TEXT,                                                                                                                                
#                                                                                                                                         Tender_Summery TEXT,
#                                                                                                                                         Tender_Details TEXT,
#                                                                                                                                         Bid_deadline_2 TEXT,
#                                                                                                                                         Documents_2 TEXT,
#                                                                                                                                         TenderListing_key TEXT,
#                                                                                                                                         Notice_Type TEXT,
#                                                                                                                                         Competition TEXT,
#                                                                                                                                         Purchaser_Name TEXT,
#                                                                                                                                         Pur_Add TEXT,
#                                                                                                                                         Pur_State TEXT,
#                                                                                                                                         Pur_City TEXT,
#                                                                                                                                         Pur_Country TEXT,
#                                                                                                                                         Pur_Email TEXT,
#                                                                                                                                         Pur_URL TEXT,
#                                                                                                                                         Bid_Deadline_1 TEXT,
#                                                                                                                                         Financier_Name TEXT,
#                                                                                                                                         CPV TEXT,
#                                                                                                                                         scannedImage TEXT,
#                                                                                                                                         Documents_1 TEXT,
#                                                                                                                                         Documents_3 TEXT,
#                                                                                                                                         Documents_4 TEXT,
#                                                                                                                                         Documents_5 TEXT,
#                                                                                                                                         currency TEXT,
#                                                                                                                                         actualvalue TEXT,
#                                                                                                                                         TenderFor TEXT,
#                                                                                                                                         TenderType TEXT,
#                                                                                                                                         SiteName TEXT,
#                                                                                                                                         createdOn TEXT,
#                                                                                                                                         updateOn TEXT,
#                                                                                                                                         Content TEXT,
#                                                                                                                                         Content1 TEXT,
#                                                                                                                                         Content2 TEXT,
#                                                                                                                                         Content3 TEXT,
#                                                                                                                                         DocFees TEXT,
#                                                                                                                                         EMD TEXT,
#                                                                                                                                         OpeningDate TEXT,
#                                                                                                                                         Tender_No TEXT)""") 
                                                                                                                                                                                                                                                                
    # cursor.execute("INSERT INTO" + file_name + "(Tender_Summery, Tender_Details, OpeningDate, Bid_deadline_2, Documents_2, Pur_URL) VALUES (?, ?, ?, ?, ?, ?)", (Tender_Summery, Tender_Details, OpeningDate, Bid_deadline_2, Documents_2, Pur_URL))                                                                                                                                       
    # cnxn.commit()
    # cnxn.close()