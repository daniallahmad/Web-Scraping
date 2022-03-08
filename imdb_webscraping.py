import requests
from bs4 import BeautifulSoup
# import gsheet
import time
import xlrd
import xlsxwriter

url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
title = []
year = []
rating = []
# wb = xlsxwriter.Workbook('imdb.xlsx')
# ws = wb.add_worksheet()


def get_title(soup):
    for i in soup.findAll(class_="titleColumn"):
        for text in i.find_all('a'):
            data = text.text
            title.append(data)


def get_year(soup):
    for i in soup.find_all(class_="secondaryInfo"):
        data = i.text
        data = data.replace('(', '').replace(')', ' ').replace('\n', '')
        data = data.strip()
        if len(data) == 4:
            year.append(data)


def get_rating(soup):
    for i in soup.findAll(class_="ratingColumn imdbRating"):
        for rate in i.find_all('strong'):
            rat = rate.text
            rating.append(rat)


# def show():
#     count = 2
#     for i, j, k in zip (title, year, rating):
#         print(i, ", ", j, " ,", k)
#         ws.write(count, 0, i)
#         ws.write(count, 1, j)
#         ws.write(count, 2, k)
#         gsheet.sheet.update_cell(count, 1, i)
#         gsheet.sheet.update_cell(count, 2, j)
#         gsheet.sheet.update_cell(count, 3, k)
#         time.sleep(5)
#         count = count + 1


get_title(soup)
get_year(soup)
get_rating(soup)
print(title)
print(year)
print(rating)

# show()
# wb.close()