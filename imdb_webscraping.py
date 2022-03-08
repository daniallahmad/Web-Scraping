# import libraries
import requests
from bs4 import BeautifulSoup
import time


url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'   # Enter the Url of the page
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
title = []
year = []
rating = []


def get_title(soup):         # function to get title of movies
    for i in soup.findAll(class_="titleColumn"):
        for text in i.find_all('a'):
            data = text.text
            title.append(data)


def get_year(soup):          # function to get year of movies
    for i in soup.find_all(class_="secondaryInfo"):
        data = i.text
        data = data.replace('(', '').replace(')', ' ').replace('\n', '')
        data = data.strip()
        if len(data) == 4:
            year.append(data)


def get_rating(soup):          # function to get rating of movies
    for i in soup.findAll(class_="ratingColumn imdbRating"):
        for rate in i.find_all('strong'):
            rat = rate.text
            rating.append(rat)


get_title(soup)
get_year(soup)
get_rating(soup)

# print all results

print(title)
print(year)
print(rating)
