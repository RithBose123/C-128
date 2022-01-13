import requests
import pandas
url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
from bs4 import BeautifulSoup as bs
page=requests.get(url)
soup=bs(page.text,"html.parser")
star_table=soup.find_all("table")
table_rows=star_table[7].find_all("tr")
templist=[]
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    templist.append(row)
Star_names = []
Distance =[]
Mass = []
Radius =[]
for i in range(1,len(templist)):
    Star_names.append(templist[i][0])
    Distance.append(templist[i][5])
    Mass.append(templist[i][7])
    Radius.append(templist[i][8])
df2 = pandas.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),
                   columns=['Star_name','Distance','Mass','Radius'])
df2.to_csv('dwarf_stars.csv')