from  bs4 import BeautifulSoup #as bs
import requests, lxml
import pandas as pd

#search_url = f'https://www.best-cd-price.co.uk/product/B006CNR0HA-No5-Collaborations-Project.html'
search_url=f'http://geminis.si2.cl:8080/#/indices'
#print (search_url)
pagina=  requests.get(search_url)

bs = BeautifulSoup(pagina.text, 'lxml')

print(bs)

#tabla = bs.find("table").find("script")
#find_all("tr",valign="baseline")

#print(tabla)
