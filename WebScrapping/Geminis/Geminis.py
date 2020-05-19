from  bs4 import BeautifulSoup #as bs
import requests, lxml
import pandas as pd

# BLOQUE DE LOGIN AL SISTEMA
login_url ='http://geminis.si2.cl:8020/auth/login'
data = {
    'username' : '023604-S'
    'password' : 'Polux9leo.'
}

with requests.session() as s:
    response= requests.post(login_url , data)
    print (response.text)
    index_page= s.get('http://geminis.si2.cl:8080/#/indices')
    soup = BeautifulSoup(index_page.text, 'html.parser')
    print (soup.title)


#search_url=f'http://geminis.si2.cl:8080/#/indices'
#pagina=  requests.get(search_url)
#bs = BeautifulSoup(pagina.text, 'lxml')
#print(bs)
