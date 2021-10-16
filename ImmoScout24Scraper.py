# import libraries
from bs4 import BeautifulSoup

# storing all the file names in a list so that we access multiple files
fileNames = ["Gepflegtes Chalet mit großartigem Grundstück und Meerblick in Sa Torre.html",
             "Gepflegtes Endreihenhaus in Strandnähe!.html",
             "Idyllisch gelegenes Haus mit herrlicher Gartenanlage.html",
             "Traumhafte, neu renovierte Naturstein-Finca in Stadtnähe.html"]


class Property:
    def __init__(self, fileName):
        self.fileName = fileName
        self.soup = None
        self.title = None
        self.address = None
        self.price = None
        self.zi = None
        self.wohnflache = None
        self.grundstuck = None

    def openProduct(self):
        with open(self.fileName) as file: # opening file
            contents = file.read()
        self.soup = BeautifulSoup(contents, 'lxml')

    def getTitle(self):
        title = self.soup.find(name="h1")
        print(title.text)

    def getAddress(self):
        address = self.soup.find(class_="address-block")
        data = address.text
        data = data.replace('\n', '').replace("    ", "")
        print(data.strip())

    def getPrice(self):
        price = self.soup.find(class_="is24qa-kaufpreis-main is24-value font-semibold is24-preis-value")
        data = price.text
        data = data.replace("â‚¬", "€")
        print(data.strip())

    def getZi(self):
        zi = self.soup.find(class_="is24qa-zi-main is24-value font-semibold")
        data = zi.text
        print("Zi :", data.strip())

    def getWohnflache(self):
        wohnflache = self.soup.find(class_="is24qa-wohnflaeche-main is24-value font-semibold")
        data = wohnflache.text
        print("Wohnfläche :", data.strip())

    def getGrundstuck(self):
        grundstuck = self.soup.find(class_="is24qa-grundstueck-main is24-value font-semibold")
        data = grundstuck.text
        print("Grundstück :", data.strip())

# using loop to access all the files in the list


for i in fileNames:
    abc = Property(i) # creating object
    abc.openProduct()
    abc.getTitle()
    abc.getAddress()
    abc.getPrice()
    abc.getZi()
    abc.getWohnflache()
    abc.getGrundstuck()
