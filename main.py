from bs4.element import TemplateString
from bs4 import BeautifulSoup
import requests

import time
import csv
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

browser = requests.get(url)
print(browser)

def Scrape():
    Headers = ["Name", "Radius", "Mass" "Distance"]

    Soup = BeautifulSoup(browser.text, "html.parser")
    
    Table = Soup.find_all("table")
    print(Table[5])
    TableRows = Table[5].find_all("tr")
    print(TableRows)

    tempList = []

    for trTags in TableRows:
        tdTags = trTags.find_all("td")

        row = [i.text.rstrip() for i in tdTags]
        tempList.append(row)

        Name = []
        Distance = []
        Mass = []
        Radius = []

        for i in range(1, len(tempList)):
            Name.append((tempList[i][0]))
            Distance.append((tempList[i][5]))
            Mass.append((tempList[i][8]))
            Radius.append((tempList[i][9]))

        df2 = pd.DataFrame(list(zip(Name, Distance, Mass, Radius)), columns=['Name', 'Distance', 'Mass', 'Radius'])
        print(df2)
        df2.to_csv('Output.csv')

Scrape()

# from bs4 import BeautifulSoup

# import requests
# import csv

# url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
 
# browser = requests.get(url)

# Header = ["Name", "Disstance Data", "Mass", "Radius"]
# Data = []

# def Scrape():
#     Soup = BeautifulSoup(browser.page_source, "html.parser")

#     for index, table in enumerate(Soup.find_all("table")):        
#         if index == 8:
#             for index, column in enumerate(table.find_all("td")):
#                 tempList = []

#                 if index == 0:
#                     tempList.append(column.contents[0].contents[0])
#                 if index == 5:
#                     tempList.append(column.contents[0])
#                 if index == 8:
#                     tempList.append(column.contents[0])
#                 if index == 9:
#                     tempList.append(column.contents[0])

#                 print(tempList)
#                 Data.append(tempList)
#             # print(table.find_all("td")[13].contents[0])
        
#         # print(index)
#         print(Data)
        
# with open("Final.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerow(Header)
#     writer.writerow(Data)

# Scrape()