# import numpy as np
# import pandas as pd
# import requests

# count = 0
# df = pd.read_excel('C:\Anjali\Kunti Tenders\Khunti.xlsx')
# row_count = print(len(df))

# for col in df.columns:

#     for url in df[col]:

#         ##check if the url has .pdf extension
#         if '.pdf' in url:
#             filename = url
#             r = requests.get(filename)

#             if r.status_code == 200:
#                 print(filename)
#                 count = count + 1
                
#                 for i in range(0, count):
#                     with open("C:\Anjali\Use_Code\Down_File_Manualy_" + str(i) + ".pdf", 'wb') as f:
#                         f.write(r.content)