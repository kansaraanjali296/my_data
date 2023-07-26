import requests
import os
from datetime import datetime


links = "https://pgimer.edu.in/PGIMER_PORTAL/AbstractFilePath?FileType=E&FileName=civ11Jul2023170943.pdf&PathKey=TENDER_PATH"
# x = requests.head(links).headers
# print(x)


files_dir = r"C:\Users\kansara.anjali\Desktop\test"
if os.path.exists(files_dir):
    pass
else:
    os.makedirs(files_dir)


def download_pdf(links):
    try:
    #----------------------------------------------download one pdf-------------------------------------------------#
        response = requests.get(links)
        print(response.status_code)
        fullname = os.path.join(files_dir, datetime.now().strftime(f"%d%m%Y_%H%M%S%f") + "." + links.rsplit('.', 1)[-1])
        # fullname = os.path.join(files_dir, datetime.now().strftime(f"%d%m%Y_%H%M%S%f") + ".pdf")
        pdf = open(fullname, 'wb')
        pdf.write(response.content)
        pdf.close()
        # logging.info("File Downloaded")

        return fullname
    except Exception as e:
        print(e)


try:
    Documents_2 = download_pdf(links)
    if Documents_2 == None:
        Documents_2 = ''
    print(Documents_2)
    # logging.info("Document :-  %s\n", Documents_2)
except Exception as e:
    Documents_2 = ''
    # logging.info("Document is not Available :- %s\n", e)

