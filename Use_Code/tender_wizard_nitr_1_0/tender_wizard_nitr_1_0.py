############################
# reduced sleep time , download files
############################
# import pytest
import time
import os
from datetime import datetime, date
from zipfile import ZipFile as zipf
import shutil
import sqlite3
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import re
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
import traceback
import pyodbc

# getLogger() method takes the test case name as input
logger = logging.getLogger(__name__)
# FileHandler() method takes location and path of log file
fileHandler = logging.FileHandler(os.path.basename(__file__) + '.log')
# Formatter() method takes care of the log file formatting
formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
fileHandler.setFormatter(formatter)
# addHandler() method takes fileHandler object as parameter
logger.addHandler(fileHandler)
logger.setLevel(logging.INFO)

logger.info("Data Extraction Started...")

start_time = time.time()
# x = datetime.datetime.now()
now = datetime.now()
dt_string = now.strftime("%d%m%Y%H%M%S")


# FileList = os.path.basename(__file__)
# global dbName
# dbName=os.path.splitext(FileList)[0]

#################################################

def wait():
    driver.implicitly_wait(6)


################################################
def rm_files(filepath):
    for f in os.listdir(filepath):
        os.remove(os.path.join(filepath, f))
################################################
def date_convert(d):
    d = d.replace(" ", "-")
    dt = datetime.strptime(d, '%d-%b-%Y').strftime('%d-%m-%Y')
    return dt


#################################################

def wait_for_downloads(filepath):
    time.sleep(2)
    print("d-", end="")
    ext = [".tmp",".crdownload"]
    while any([filename.endswith(tuple(ext)) for filename in
               os.listdir(os.path.join(os.environ['USERPROFILE'], filepath))]):
        time.sleep(2)
        print(".", end="")
        wait()
    print("done!")


#################################################
def rename(filepath, pdf_or_zip_wloc):
    # filepath = os.path.join(os.environ['USERPROFILE'], "Downloads")
    time.sleep(1)
    try:
        filename = max([filepath + "\\" + f for f in os.listdir(filepath)], key=os.path.getctime)
        print(filename)
    except:
        logger.info('file not found in temp folder')
        print("file not found")
    # print(filename1)

    # curr = date_time()
    if os.path.exists(filename):
        # newname = os.path.join(dir, "ap_" + curr + ".zip")
        if '.zip' in filename:
            pdf_or_zip_wloc.replace(".pdf", ".zip")
            os.rename(filename, pdf_or_zip_wloc)
        elif '.doc' in filename:
            pdf_or_zip_wloc.replace(".pdf", ".doc")
        else:
            os.rename(filename,pdf_or_zip_wloc)

    else:
        print("file not found")


#################################################
def download_pdf(filepath, pdf_or_zip_wloc):
    for a in driver.find_elements(By.XPATH, '//a[contains(.,"Download")]'):
##        a.click()
##        a =  driver.find_element(By.XPATH, '//th[contains(.,"Document Name")]//following::li//a[contains(.,"Download")]')
        driver.execute_script("arguments[0].click();", a)
        # 2 seconds sleep  - waiting for download to start
        time.sleep(2.5)
        wait_for_downloads(filepath)
        time.sleep(1)
        zipp(pdf_or_zip_wloc)
        wait()    
        print("..")



def zipp(pdf_or_zip_wloc):
    filename = max([filepath + "\\" + f for f in os.listdir(filepath)], key=os.path.getctime)
    print(filename)
    with zipf(pdf_or_zip_wloc, "a") as zipobj:
        zipobj.write(filename, os.path.basename(filename))

##############################################
def check_tender_dup(i):
    print("..")


#############################################

def RemoveExtraSpace(string):
    new = re.sub(' +', ' ', string)
    return new


##############################################
def db_sql(pagelist, table_name):
    insert = 'insert into ' + table_name + '(Tender_Notice_No, Tender_Summery, Documents_2, Purchaser_Name,actualvalue,DocFees,EMD,Pur_Add, Pur_Country, Pur_Email, Pur_URL, currency, TenderType, createdOn,Content, OpeningDate, Bid_deadline_2, DupFlag) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    cursor.executemany(insert, pagelist)
    conn.commit()
    logger.info("data inserted into sqlite")
    #####
    all = cursor2.execute('SELECT Tender_Notice_No, Tender_Summery, Documents_2, Purchaser_Name,actualvalue,DocFees,EMD,Pur_Add, Pur_Country, Pur_Email, Pur_URL, currency, TenderType, Content, OpeningDate, Bid_deadline_2 FROM ' + table_name + ' where DupFlag = 1')
    # print("***", all)
    #####
    
    
    cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=192.168.100.153;'
                      'Database=CrawlingDB;'
                      'uid=meet;' 'PWD=meet@123;')

    
    for row in cursor2:
        fname =url.split('/')
        file_name = fname[2]#+".csv"
        newName = file_name.replace('.','_')+"_NITRpy_TenderListing"
        cursor1 = cnxn.cursor()
        idName = newName+" ID"
        cursor1.execute('''
                            IF  NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[{0}]') AND type in (N'U'))
                            begin
                            CREATE TABLE "{0}"( "{1}" UNIQUEIDENTIFIER DEFAULT NEWID() PRIMARY KEY,Tender_Notice_No nvarchar(4000), Tender_Summery nvarchar(4000), Tender_Details nvarchar(4000), Bid_deadline_2 nvarchar(4000), Documents_2 nvarchar(4000), TenderListing_key nvarchar(4000), Notice_Type nvarchar(4000), Competition nvarchar(4000), Purchaser_Name nvarchar(4000), Pur_Add nvarchar(4000), Pur_State nvarchar(4000), Pur_City nvarchar(4000), Pur_Country nvarchar(4000), Pur_Email nvarchar(4000), Pur_URL nvarchar(4000),Bid_Deadline_1 nvarchar(4000),Financier_Name nvarchar(4000),CPV nvarchar(4000),scannedImage nvarchar(4000),Documents_1 nvarchar(4000),Documents_3 nvarchar(4000),Documents_4 nvarchar(4000),Documents_5 nvarchar(4000),currency nvarchar(4000),actualvalue nvarchar(4000),TenderFor nvarchar(4000),TenderType nvarchar(4000),SiteName nvarchar(4000),createdOn nvarchar(4000),updateOn nvarchar(4000),Content varchar(max),Content1 nvarchar(4000),Content2 nvarchar(4000),Content3 nvarchar(4000),DocFees nvarchar(4000),EMD nvarchar(4000),OpeningDate nvarchar(4000),Tender_No nvarchar(4000))
                            end'''.format(newName,idName))
        cursor1.execute('''BEGIN
                            INSERT INTO "{0}" (Tender_Notice_No, Tender_Summery, Documents_2, Purchaser_Name,actualvalue,DocFees,EMD,Pur_Add, Pur_Country, Pur_Email, Pur_URL, currency, TenderType, Content, OpeningDate, Bid_deadline_2)
                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                            END'''.format(newName),
                            row[0]
                            ,row[1]
                            ,row[2]
                            ,row[3]
                            ,row[4]
                            ,row[5]
                            ,row[6]
                            ,row[7]
                            ,row[8]
                            ,row[9]
                            ,row[10]
                            ,row[11]
                            ,row[12]
                            ,row[13]
                            ,row[14]
                            ,row[15])
        cnxn.commit()
    cnxn.close()
    #####
    logger.info('Server - data inserted')

    cursor.execute('UPDATE ' + table_name + ' set DupFlag = 0 where DupFlag = 1')
    conn.commit()
    logger.info("data updated - sqlite")


##############################################
def date_time():
    date_time = []
    date_time = str(datetime.now())
    date_time = date_time.replace(' ', '_')
    date_time = date_time.replace('-', '')
    date_time = date_time.replace(':', '')
    date_time = date_time.replace('.', '')
    return date_time


####################################
def connect():
    print("con")
####################################
def scrape(pdf_or_zip_wloc,dn_flag):
    try:
        #pagelist = []
            try:
                '''Tender_Summery = driver.find_element(By.XPATH,
                                                     '//td[contains(.,"Detailed Description")]//following::td').text.strip()'''
                Tender_Summery = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, '//td[contains(.,"Description Of Work:")]//following::td'))).text
            except Exception as e:
                print(e)
                Tender_Summery = ''
                print('no ts')
                logger.info('cannot find Tender_Summery')

            try:
                '''Tender_Notice_No = driver.find_element(By.XPATH,
                                                       '//td[contains(.,"Tender Reference")]//following::td').text.strip()'''
                Tender_Notice_No = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, '//td[contains(.,"Tender:")]//following::td'))).text.strip()
                print(Tender_Notice_No)


            except Exception as e:
                print(e)
                print('no tn')
                Tender_Notice_No = ''
                logger.info('cannot find Tender_Notice_No')


            wait()
            try:
                Content = driver.find_element(By.XPATH, '//*[@id="tenderDetail"]')
                Content = Content.get_attribute('innerHTML')
            except Exception as e:
                print(e)
                logger.info('content cannotfind element')
                Content = ''

            try:
##                Pur_Add = driver.find_element(By.XPATH, '//td[contains(.,"Region:")]//following::td').text.strip()
                Pur_Add = 'National Institute of Technology Raipur'
            except:
                Pur_Add = ''
                print('no add')
                logger.info('cannot find Pur_Add')

            try:
                Pur_Email = driver.find_element(By.XPATH, '//td[contains(.,"Email:")]//following::td').text.strip()
            except:
                print('no email')
                Pur_Email = ''
                logger.info('cannot find Pur_Email')


            try:
                TenderType = driver.find_element(By.XPATH,
                                                 '//td[contains(.,"Interest")]//following::td').text.strip()
            except:
                print('no ttype')
                TenderType = ''
                logger.info('cannot find TenderType')
                
            if dn_flag == 0:
                Documents_2 = ''
            else:
                Documents_2 = pdf_or_zip_wloc

            try:
                actualvalue = driver.find_element(By.XPATH,
                                              '//td[contains(.,"Estimated Cost")]//following::td').text.split()[0].strip().replace(',','')
            except:
                print('no avalue')
                actualvalue = ''

            try:
                DocFees = driver.find_element(By.XPATH,
                                              '//td[contains(.,"Processing Fee")]//following::td').text.split()[0].strip().replace(',','')
            except:
                print('no docfees')
                DocFees = ''

            try:
                EMD = driver.find_element(By.XPATH,
                                              '//td[contains(.,"EMD")]//following::td').text.split()[0].strip().replace(',','')
            except:
                print('no emd')
                EMD = ''

            try:
                OpeningDate = driver.find_element(By.XPATH,
                                                  '//td[contains(.,"Issue of Tender")]//following::td').text.split()[0]
##                OpeningDate = ''
            except:
                OpeningDate = ''
                print('no Opendate')
                logger.info('cannot find OpeningDate')

            try:
                Bid_deadline_2 = driver.find_element(By.XPATH,
                                                     '//td[contains(.,"Closing")]//following::td').text.split()[0].strip().replace('-','/')
            except:
                Bid_deadline_2 = ''
                print('no bd2')
                logger.info('cannot find Bid_Deadline_2')



            Pur_Country = 'India'
            Purchaser_Name = 'National Institute of Technology Raipur'
            createdOn = datetime.now().strftime('%d-%b-%Y')
            DupFlag = '1'
            currency = 'INR'
            Pur_URL =  'https://www.tenderwizard.in/ROOTAPP/Mobility/index.html?dc=encDvhGP4TEWElwrPjOFHeB5Q==#/home'
            wait()

            logger.info('zip file - %s', pdf_or_zip_wloc)

            onelist = [Tender_Notice_No, Tender_Summery, Documents_2, Purchaser_Name,actualvalue,DocFees,EMD,
                       Pur_Add, Pur_Country, Pur_Email, Pur_URL, currency, TenderType, createdOn,
                       RemoveExtraSpace(Content), OpeningDate, Bid_deadline_2, DupFlag]
            #pagelist.append(onelist)
            # print(pagelist)

            # shutil.rmtree(dir)
            return onelist


    except:
        print(traceback.format_exc())
        print('error heree')
        # db_sql(pagelist, table_name)



####################################
# def crawl_data():
####################################
# def check_duplicate():
#########################################################################
url = 'https://www.tenderwizard.in/ROOTAPP/Mobility/index.html?dc=encDvhGP4TEWElwrPjOFHeB5Q==#/home'

hostname = url.split('/')[2] + "_NITRpy"
dir = os.path.join(os.environ['USERPROFILE'], "My Documents") + "\\" + "python_files\\" + hostname + "\\" + "files"
filepath = os.path.join(os.environ['USERPROFILE'],
                        "My Documents") + "\\" + "python_files\\" + hostname + "\\" + "temp file"

# dirpath = os.path.join(os.environ['USERPROFILE'], "Downloads") #not tested after changing
if not os.path.isdir(filepath):
    print("temp file dir not exists")
    os.makedirs(filepath)
else:
    print("temp file dir exists")

if not os.path.isdir(dir):
    print("files dir not exists")
    os.makedirs(dir)
else:
    print("files dir exists")
#########################################################################
database = hostname.replace('.', '_') + ".db"
table_name = hostname.replace('.', '_')

conn = sqlite3.connect(database)
# conn.row_factory = lambda cursor, row: row[0]
cursor = conn.cursor()
cursor.row_factory = lambda cursor, row: row[0]
cursor2 = conn.cursor()
create = 'create table IF NOT EXISTS ' + table_name + '(Id INTEGER PRIMARY KEY,Tender_Notice_No TEXT,Tender_Summery TEXT,Tender_Details TEXT,Bid_deadline_2 TEXT,Documents_2 TEXT,TenderListing_key TEXT,Notice_Type TEXT,Competition TEXT,Purchaser_Name TEXT,Pur_Add TEXT,Pur_State TEXT,Pur_City TEXT,Pur_Country TEXT,Pur_Email TEXT,Pur_URL TEXT,Bid_Deadline_1 TEXT,Financier_Name TEXT,CPV TEXT,scannedImage TEXT,Documents_1 TEXT,Documents_3 TEXT,Documents_4 TEXT,Documents_5 TEXT,currency TEXT,actualvalue TEXT,TenderFor TEXT,TenderType TEXT,SiteName TEXT,createdOn TEXT,updateOn TEXT,Content TEXT,Content1 TEXT,Content2 TEXT,Content3 TEXT,DocFees TEXT,EMD TEXT,OpeningDate TEXT,Tender_No TEXT,DupFlag TEXT)'
cursor.execute(create)
#########################################################################
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    "download.default_directory": filepath,  # Change default directory for downloads
    "download.prompt_for_download": False,  # To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": False  # It will not show PDF directly in chrome
})
options.add_argument('--no-sandbox')
# chrome_options.add_argument('headless')
options.add_argument('--ignore-certificate-errors')
ser = Service(r'C:\Users\meet.nayani\PycharmProjects\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=ser, options=options)
logger.info("Data Extraction Started...")
driver.get(url)
driver.implicitly_wait(30)
time.sleep(2)
# close pop up window
driver.find_element(By.XPATH,'/html/body/ux-dialog-container/div/div/div/div[1]/div[2]').click()
main = driver.window_handles[0]
driver.switch_to.window(main)
# click to active tenders-----------1
active_tenders = driver.find_element(By.XPATH,'//*[@id="divSubMasterContainer"]/div/div[1]/div/div/div[1]/div[2]/div[2]')
driver.execute_script("arguments[0].click();", active_tenders)

wait()
time.sleep(5)
win1 = driver.window_handles[1]
driver.switch_to.window(win1)
wait()
driver.maximize_window()
captcha = input('enter captcha')
time.sleep(8)
driver.find_element(By.XPATH,'//*[@id="UserEnteredCaptcha"]').send_keys(captcha)
try:
    # submit after entering captcha
    driver.find_element(By.XPATH, '//*[@id="btnSubmit"]').click()
except:
    print('user manually submitted ')
wait()
time.sleep(2)

count = 1
scraped = 1
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
total_pages = driver.find_element(By.XPATH,'//*[@id="uipage"]//a[last()-1]').text
print(total_pages)
for curr_page_number in range(1, int(total_pages) + 1):
    tnum = 1
    pagelist = []
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    row_len = len(driver.find_elements(By.XPATH, '//a[contains(.,"Action")]'))
    print('rows:',row_len)
    tns = driver.find_elements(By.XPATH,'//*[@id="tblSummary"]/tbody/tr/td[3]')
    tss = driver.find_elements(By.XPATH,'//*[@id="tblSummary"]/tbody/tr/td[5]')
    links = driver.find_elements(By.XPATH,'//*[@id="tblSummary"]/tbody/tr/td[2]//a')
    #for i in range(2, row_len + 1):
    for tnn,ts,link in zip(tns,tss,links):  
        try:
            print(curr_page_number,".", tnum)
            tnum = tnum + 1
            try:  # get title and tender notice number
                #tnn = driver.find_element(By.XPATH, '//*[@id="tblSummary"]/tbody/tr[' + str(i) + ']/td[3]').text.strip()
                #ts = driver.find_element(By.XPATH, '//*[@id="tblSummary"]/tbody/tr[' + str(i) + ']/td[5]').text.strip()
                tnn = tnn.text
                ts = ts.text
            except Exception as e:
                print(e)
                logger.info('error in reading table for checking dup')
                print("cant check for dup ! error")
            print(tnn,ts)

            try:
                check = cursor.execute(
                    'SELECT EXISTS(SELECT 1 FROM ' + table_name + ' WHERE Tender_Notice_No = ?)', (tnn,)).fetchone()
                print(check)
            except Exception as e:
                print(e)
                print('dup check error')
            if check == 0:
                try:
                    #driver.find_element(By.XPATH, '//*[@id="tblSummary"]/tbody/tr[' + str(i) + ']/td[2]/a').click()
##                    link.click()
                    driver.execute_script("arguments[0].click();", link)
                    wait()
                    # a.click()
                    driver.find_element(By.XPATH, '//*[@id="action-links"]/ul/li[1]/a').click()
##                    driver.implicitly_wait(20)
##                    driver.switch_to.alert.accept()
                    wait()

                except:
                    tb = traceback.format_exc()
                    print(tb)
                    print('cannot click this link')
                time.sleep(1)
                win2 = driver.window_handles[2]
                driver.switch_to.window(win2)
                wait()
                driver.maximize_window()
                curr = date_time()
                pdf_or_zip_wloc = os.path.join(dir, "wizard_NITR_" + str(curr) + ".zip")
                # download files here
                try:    
                    download_pdf(filepath, pdf_or_zip_wloc)
                    dn_flag = 1
                except Exception as e:
                    tb = traceback.format_exc()
                    print(tb)
                    dn_flag = 0
                    logger.info("doc not found / unable to download doc")
                    print("tf1x")
                    

                # click to detail page--------------3
                WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//table//a'))).click()
                driver.implicitly_wait(20)
                time.sleep(1)
                win3 = driver.window_handles[3]
                driver.switch_to.window(win3)
                wait()
                driver.maximize_window()

                time.sleep(0.5)
                # click for more details on same page

                try:
                    WebDriverWait(driver, 1).until(
                        EC.element_to_be_clickable((By.XPATH, '//a[contains(.,"Show Tender Details")]'))).click()
                    # driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[3]/form/div[2]/a').click()
                    driver.implicitly_wait(20)
                except:
                    print('')

                '''if len(driver.find_elements(By.XPATH,'//a[.,"Show Tender Detail"]')) > 0 :
                    driver.find_element(By.XPATH, '//a[.,"Show Tender Detail"]').click()'''

                # time.sleep(1.5)
                onelist = scrape(pdf_or_zip_wloc,dn_flag)
                pagelist.append(onelist)
                # db_sql(onelist, table_name)
                print("T_SCRAPED", scraped)
                scraped = scraped + 1
                driver.close()
                driver.switch_to.window(win2)
                driver.close()
                driver.switch_to.window(win1)
                rm_files(filepath)
            else:
                print("dup")
                continue

            print("---------------------------------------------------")
        except Exception as e:
            tb = traceback.format_exc()
            print(tb)
            print(e)
            print('exception from win2')
    try:
        db_sql(pagelist,table_name)
    except Exception as e:
        tb = traceback.format_exc()
        print(tb)
        print(e)
        print('db_Sql error')
    try:
        pg = curr_page_number + 1
        driver.find_element(By.XPATH,'//*[@id="uipage"]/div[2]/div[2]/form/div[3]/div/a['+str(pg)+']').click()
    except Exception as e:
        tb = traceback.format_exc()
        print(tb)
        print(e)
        print('pagenataion error')

logger.info('all tenders scraped')
#time.sleep()

startTime = datetime.now()
print(startTime)
wait()
pop = driver.window_handles[0]
driver.switch_to.window(pop)
driver.quit()
# time.sleep(15)
#
# driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/a[1]').click()
# wait()
#########################################################################
# WebDriverWait(driver,10).until(EC.element_located_to_be_selected(()))
#########################################################################


logger.info("Data Extraction Completed %s", (time.time() - start_time))
logger.info("Data Extraction Completed")
