#importing libraries
import requests  #importing request to open web url
from bs4 import BeautifulSoup #using beautiful soup for getting data


k = 1
while k <= 10:
    url = 'https://quotes.toscrape.com/page/'+str(k)+'/' #url to be scraped
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
        print(quote)
        print(author)
        print(tag)
        i = i+1
        time.sleep(5)
    k = k+1
