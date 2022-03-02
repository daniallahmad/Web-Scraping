# lib imports

from selenium import webdriver
import time
import urllib.request
import json
import requests

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(executable_path=PATH)
r = "https://www.daraz.pk/laptops/"
driver.get(r)


class Products: # making class of product & using all the functions in it
    def __init__(self, url):
        self.url = url
        self.title = None
        self.price = None
        self.brand = None
        self.sku = None
        self.imageUrls = None
        self.imageDownload = None
        self.downloadFolder = None
        self.uploadImg = None

    def openProduct(self):
        driver.get(self.url)

    def getTitle(self):
        title = driver.find_element_by_id("module_product_title_1")
        titleText = title.text
        self.title = '{0}'.format(titleText).strip()

    def getPrice(self):
        price = driver.find_element_by_id("module_product_price_1")
        priceText = price.text
        self.price = '{0}'.format(priceText)

    def getBrand(self):
        brand = driver.find_elements_by_class_name('key-li')
        for i in brand:
            if i.find_element_by_class_name('key-title').text == 'Brand':
                self.brand = i.find_element_by_class_name('html-content.key-value').text
                break

    def getSKU(self):
        sku = driver.find_elements_by_class_name('key-li')
        for i in sku:
            if i.find_element_by_class_name('key-title').text == 'SKU':
                self.sku = i.find_element_by_class_name('html-content.key-value').text
                break

    def getImageUrls(self): # function to get all the image src urls
        l = []
        imgUrls = driver.find_elements_by_tag_name('img')
        for img in imgUrls[4:]:
            x = img.get_attribute('src')
            if 'webp' in x:
                x = x.replace('120x120', '720x720') # converting all the images to 720'px
                l.append(x)
            if 'png' in x:
                break
        self.imageUrls = l

    def getImgDownloaded(self): # function for downloading the image using url
        list = []
        for i in self.imageUrls:
            fullPath = "image_" + i.replace('https://', '').replace('.jpg_.webp', '.jpg').replace('.daraz.pk/p/', "")
            (urllib.request.urlretrieve(i, fullPath))
            list.append(fullPath)
            self.imageDownload = list

    def getUploadDrive(self): # function to upload image in google drive
        headers = {
            "Authorization": "Bearer ######enter access token from google drive api####"}
        for i in self.imageDownload:
            para = {
                "name": i,
                "parents": ["1GjxFwgM235BdxuOD7fOLccsTUbtABRE6"] # Google folder id 
            }
            files = {
                'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
                'file': open(i, "rb")
            }
            r = requests.post(
                "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                headers=headers,
                files=files
            )


# function for getting all the product urls
def getUrls(url):
    listOfUrls = []
    for i in range(1, 41):
        list = driver.find_elements_by_xpath(
            "//*[@id='root']/div/div[3]/div[1]/div/div[1]/div[2]/div[" + str(i) + "]/div/div/div[1]/div/a[@href]")
        for j in list:
            listOfUrls.append(j.get_attribute("href"))
        i = i + 1

    time.sleep(3)
    return listOfUrls

# making a object of the class
listOfUrls = getUrls('https://www.daraz.pk/laptops/')
o = Products(listOfUrls[0])
o.openProduct()
o.getTitle()
o.getPrice()
o.getBrand()
o.getSKU()
o.getImageUrls()
o.getImgDownloaded()
o.getUploadDrive()
# use the print() to view the results
driver.quit()
