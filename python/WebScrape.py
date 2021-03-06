import bs4
import requests
from urllib.request import urlopen
import sys

#automated links
res = requests.get("http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/default.aspx")
webSoup = bs4.BeautifulSoup(res.text, "lxml")

urls = []

for link in webSoup.find_all('a'):
    urls.append(link.get('href'))

for i in urls:
    
    if i.startswith('/Eng'):
        url = "http://www.osfi-bsif.gc.ca"+i  
        html = urlopen(url)
        page_content = html.read()
    else:
        url = i  
        html = urlopen(url)
        page_content = html.read()
    
    with open(i.split('/')[-1]+".html", 'w+') as file_: 
        file_.write(str(page_content))

#manual links
urls = ['http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/a3.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/car_index.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CAR_chpt6_upd_let.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/LAR_index.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/LR.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/b1.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/b2.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/b3.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/b4.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/b6.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/b11_final.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/e6_dft.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/e6dti.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/ifrs9.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/c1_ifrs.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/c5_ifrs.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/d1_ifrs.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/d6_ifrs.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/d10_ifrs.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/lcr.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/LRDisc.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/plr3.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CG_Guideline.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/b7.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/b8.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/b10.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/B12_IRR_Feb2005.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/b20.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/e13.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/E17_final.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/e18.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/icaap_dti.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/e20.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/e21.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/e22.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/e4b.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/b5a.aspx',
'http://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/a10fbb.aspx',
'http://laws-lois.justice.gc.ca/eng/acts/O-2.7/FullText.html',
'http://laws-lois.justice.gc.ca/eng/acts/B-1.01/FullText.html']

CDIC = 'http://www.cdic.ca/en/financial-community/legislation-bylaws/Pages/default.aspx'

for i in urls:
    html = urlopen(i)
    page_content = html.read()
    
    with open(i.split('/')[-1], 'w+') as file_: 
        file_.write(str(page_content))

######Regs
res = requests.get("http://laws-lois.justice.gc.ca/eng/acts/B-1.01/FullText.html")
webSoup = bs4.BeautifulSoup(res.text, "lxml")   
with open('bank_act.html', 'wb') as file_: 
    file_.write(webSoup.prettify(formatter="html"))    
    
###Text Scraper
txt = webSoup.get_text()      
with open('bank_act.txt', 'w+') as file_: 
    file_.write(webSoup.prettify(formatter="none"))
   
   
webSoup.prettify(webSoup.get_text())
    
fileIn = open("d:/Users/Fred/Documents/GitHub/sdenotter.github.io/complete_list_of_federal_statutes/A-1.5.xml", 'rb')   
webSoup = bs4.BeautifulSoup(fileIn,"lxml-xml")
with open('A-1.5.txt', 'wb') as fileOut: 
    fileOut.write(webSoup.get_text().encode("utf-8")) 
    


    
res = requests.get('http://laws-lois.justice.gc.ca/eng/acts/B-1.01/20150623/P1TT3xt3.html')
webSoup = bs4.BeautifulSoup(res.text, "lxml")      
with open('previous_bank_act.html', 'wb') as file_: 
    file_.write(webSoup.prettify("utf-8")) 
    
res = requests.get('http://laws-lois.justice.gc.ca/eng/acts/O-2.7/FullText.html')
webSoup = bs4.BeautifulSoup(res.text, "lxml")  
with open('office_of_the_superintendent_of_financial_institutions_act.html', 'wb') as file_: 
    file_.write(webSoup.prettify("utf-8")) (webSoup.get_text())
    
res = requests.get('http://laws-lois.justice.gc.ca/eng/acts/O-2.7/20140619/P1TT3xt3.html')
webSoup = bs4.BeautifulSoup(res.text, "lxml")     
with open('previous_office_of_the_superintendent_of_financial_institutions_act.html', 'wb') as file_: 
    file_.write(webSoup.prettify("utf-8")) 
    
    res = requests.get('http://laws-lois.justice.gc.ca/eng/acts/O-2.7/20140619/P1TT3xt3.html')
webSoup = bs4.BeautifulSoup(res.text, "lxml")     
with open('previous_office_of_the_superintendent_of_financial_institutions_act.html', 'wb') as file_: 
    file_.write(webSoup.prettify("utf-8")) 
#NEW Regs   
res = requests.get('http://laws.justice.gc.ca/eng/regulations/SOR-2000-177/FullText.html')
webSoup = bs4.BeautifulSoup(res.text, "lxml")     
with open('Canada Deposit Insurance Corporation Notice Regulations (Compensation in Respect of the Restructuring of Federal Member Institutions).html', 'wb') as file_: 
    file_.write(webSoup.prettify("utf-8")) 
    
res = requests.get('http://laws.justice.gc.ca/eng/regulations/SOR-2007-255/FullText.html')
webSoup = bs4.BeautifulSoup(res.text, "lxml")     
with open('Eligible Financial Contract Regulations (Canada Deposit Insurance Corporation Act).html', 'wb') as file_: 
    file_.write(webSoup.prettify("utf-8")) 
    
res = requests.get('http://laws.justice.gc.ca/eng/regulations/SOR-2007-255/20160614/P1TT3xt3.html')
webSoup = bs4.BeautifulSoup(res.text, "lxml")     
with open('Previous Eligible Financial Contract Regulations (Canada Deposit Insurance Corporation Act).html', 'wb') as file_: 
    file_.write(webSoup.prettify("utf-8")) 
    
res = requests.get('http://laws.justice.gc.ca/eng/acts/F-11/FullText.html')
webSoup = bs4.BeautifulSoup(res.text, "lxml")     
with open('Financial Administration Act.html', 'wb') as file_: 
    file_.write(webSoup.prettify("utf-8")) 
    
res = requests.get('http://laws.justice.gc.ca/eng/acts/F-11/20160101/P1TT3xt3.html')
webSoup = bs4.BeautifulSoup(res.text, "lxml")     
with open('previous Financial Administration Act.html', 'wb') as file_: 
    file_.write(webSoup.prettify("utf-8")) 
    
res = requests.get('http://laws.justice.gc.ca/eng/acts/C-3/FullText.html')
webSoup = bs4.BeautifulSoup(res.text, "lxml")     
with open('Canada Deposit Insurance Corporation Act.html', 'wb') as file_: 
    file_.write(webSoup.prettify("utf-8")) 
    
res = requests.get('http://laws.justice.gc.ca/eng/acts/C-3/20140619/P1TT3xt3.html')
webSoup = bs4.BeautifulSoup(res.text, "lxml")     
with open('Previous Canada Deposit Insurance Corporation Act.html', 'wb') as file_: 
    file_.write(webSoup.prettify("utf-8")) 