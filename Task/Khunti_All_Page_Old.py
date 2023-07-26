from cgitb import text
from distutils.log import info
from attr import attrs
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from webdriver_manager.chrome import ChromeDriverManager
from numpy import tril
import pandas as pd
import bs4, re
import os
import logging
from datetime import datetime
import time


logging.basicConfig(filename='C:\Anjali\Kunti Tenders\khunti_all_page.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('Started Web Scraping')

def my_function(soup, url):
    tr_list = soup.find('tbody').find_all('tr')
    print('Total Rows:' + str(len(tr_list)))

    count = 0
    for i in tr_list:
        count = count + 1
        td_list = i.find_all('td')
        td_count = 0

        for td_all_data in td_list:
            if td_count == 0:
                Title.append(td_all_data.text)

            elif td_count == 1:
                Desc.append(td_all_data.text)

            elif td_count == 2:
                Start_date.append(td_all_data.text)

            elif td_count == 3:
                End_date.append(td_all_data.text)

            elif td_count == 4:
                link_to_file = td_all_data.find_all('a', href=True, attrs={'title':"Click here to View"})
                links = [i['href']for i in link_to_file]
                links = ', '.join(links)
                File.append(str(links))
                SourceUrl.append(url) #------------------ Source_url columnNo-5


                logging.info('Row Inserted')

                files_dir = 'C:\Anjali\Kunti Tenders\Khunti_All_Pdf'
                if not os.path.exists(files_dir):
                    os.mkdir(files_dir)

                name_of_file = links.rsplit('/', 1)[-1]
                response = requests.get(links)
                complete_name = os.path.join(files_dir, name_of_file)

                pdf = open(complete_name, 'wb')
                pdf.write(response.content)
                pdf.close()

                logging.info('Download PDF File')

            td_count = td_count + 1
            
try:

    Title = []
    Desc = []
    Start_date = []
    End_date = []
    File = []
    SourceUrl = []

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    # print('---------------------notice categories page----------------------')

    # url = 'https://khunti.nic.in/notice_category/tenders/'
    # driver.get(url)    ### selenium open url direct with driver
    # page = requests.get(url)
    # soup = BeautifulSoup(page.content, 'html.parser')
    # my_function(soup, url)
    # logging.debug(url)
    
    print('---------------------notice categories page 1 ----------------------')

    url = 'https://khunti.nic.in/past-notices/tenders/'
    driver.get(url)                                                            
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    my_function(soup, url)
    logging.debug(url)
    
    next_link = soup.find('div', class_="pegination").find('a').get('href')
    driver.get(next_link)
    logging.debug(url)

    j = 2
    while j >= 2:
        print('-----------------------past Notice Page' + str(j) + '---------------')
        page = requests.get(next_link)
        soup = BeautifulSoup(page.content, 'html.parser')
        my_function(soup,next_link)
        
        j += 1
        if soup.findAll('a', href=True, text=re.compile("Next")):
            next_link = soup.findAll('a', href=True, text=re.compile("Next"))[0]['href']
            driver.get(next_link)
            logging.debug(url)
        else:
            break
        
        break
    driver.close()
    logging.info('Finished Web Scraping')

    # print('Title-' + str(len(Title)) + ', Description-' + str(len(Desc)) + ',Start Date-' + str(len(Start_date)) + ', End Date-' + str(len(End_date)) + ', File-' + str(len(File)) + ', SourceUrl-' + str(len(SourceUrl)))
    logging.info('Create Excal File')
    df = pd.DataFrame({'Title': Title, 'Description': Desc, 'Start Date': Start_date, 'End Date': End_date, 'File': File, 'SourceUrl': SourceUrl})
    with pd.ExcelWriter('C:\Anjali\Kunti Tenders\Khunti_All_Page.xlsx') as wr:
        df.to_excel(wr, index=False)

    logging.info('All Data Saved In Excal File')
    logging.warning('Check Excal File!')

    print("\nProceed Successfully!\n")
     
except Exception as e:
    print(e)

import pandas as pd 
import sqlite3

df = pd.read_excel('C:\Anjali\Kunti Tenders\Khunti_All_Page.xlsx')

logging.info('Create Database')
connection = sqlite3.connect('C:\Anjali\Kunti Tenders\khunti_db.db')

logging.info('Insert Data Into Database')
df.to_sql(name = 'Khunti_All_Page', con = connection, if_exists= 'replace', index=False,
dtype = {'Title': 'text', 'Description': 'text', 'Start Date': 'real', 'End Date': 'real', 'File': 'text', 'SourceUrl': 'text'})

logging.info('All Data Inserted Into Database')
logging.warning('Check Database!')

connection.commit()
connection.close()

logging.info('Database close')

logging.info('Proceed Successfully Done')


