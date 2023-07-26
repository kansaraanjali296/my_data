###---------------------downoad code for any extention---------------------

# def download_file(plz get url):
import os

files_dir = 'C:\Anjali\Kunti Tenders\khunti_n'

if not os.path.exists(files_dir):
    os.mkdir(files_dir)


link_to_file = "https://skuastkashmir.co.in/frmPDF.aspx?FN=1st Answer Keyyw (1).pdf"

name_of_file = link_to_file.rsplit('/', 1)[-1]
response = requests.get(link_to_file)
complete_name = os.path.join(files_dir, name_of_file)

pdf = open(complete_name, 'wb')
pdf.write(response.content)
pdf.close()
