import PyPDF2
import requests
import csv

from tika import parser
from lxml import html

t = parser.from_file('g.pdf')

t=t['content'].splitlines()

t=t[212:8030]

a_list=[]

for i in t:
    if i=='':
        pass
    else:
        a_list.append(i)

page = requests.get('https://en.wikipedia.org/wiki/List_of_largest_California_cities_by_population')
tree = html.fromstring(page.content)


city_list = []

for i in range(102):
    city_list.append(tree.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr['+str(i)+']/td[2]/a/text()'))

city_list =city_list[2:102]

city=[]

for i in city_list:
    city.append(i.pop())

for i in city:
    file = open(i+".txt",'w')
    for j in a_list:
        file.write(i+" "+j+",")
    file.close()


