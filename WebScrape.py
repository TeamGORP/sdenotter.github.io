import bs4
import requests
from urllib.request import urlopen

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


