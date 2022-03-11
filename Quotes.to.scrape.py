import requests
from bs4 import BeautifulSoup
import gsheet
import time
k = 1
count = 2
while k <= 10:
    url = 'https://quotes.toscrape.com/page/'+str(k)+'/'
    r = requests.get(url)
    page = BeautifulSoup(r.text, 'lxml')
    i = 0
    while i < 10:
        quote = page.find_all(class_='text')[i].text.strip()
        author = page.find_all(class_='author')[i].text.strip()
        tag = page.find_all(class_='tags')[i].text.strip()
        tag = tag.replace('Tags:', '')
        tag = tag.replace('\n', ' ')
        tag = tag.strip()
        gsheet.sheet.update_cell(count, 1, quote)
        gsheet.sheet.update_cell(count, 2, author)
        gsheet.sheet.update_cell(count, 3, tag)
        i = i+1
        time.sleep(5)
        count += 1
    k = k+1