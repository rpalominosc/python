from  bs4 import BeautifulSoup #as bs
import requests, lxml
import pandas as pd

#search_url = f'https://www.best-cd-price.co.uk/product/B006CNR0HA-No5-Collaborations-Project.html'
search_url=f'http://www.bncatalogo.gob.cl/F/8SUFU8KIUNHA9H1ULP7B2VKT1T48YBVRRXVTHS3SX8R6J2MS6G-18316?func=find-b&local_base=5001&find_code=WSU&request=Biografias&adjacent=N&x=0&y=0'
#print (search_url)
pagina=  requests.get(search_url)

bs = BeautifulSoup(pagina.text, 'lxml')

tabla = bs.find("table").find("script")
#find_all("tr",valign="baseline")

print(tabla)
