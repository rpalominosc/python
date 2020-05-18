from  bs4 import BeautifulSoup #as bs
import requests, lxml
import pandas as pd

#search_url = f'https://www.best-cd-price.co.uk/product/B006CNR0HA-No5-Collaborations-Project.html'
search_url=f'http://www.bncatalogo.gob.cl/F/8SUFU8KIUNHA9H1ULP7B2VKT1T48YBVRRXVTHS3SX8R6J2MS6G-18316?func=find-b&local_base=5001&find_code=WSU&request=Biografias&adjacent=N&x=0&y=0'
print (search_url)
pagina=  requests.get(search_url)
datos = {
    'Autor' : [],
    'Titulo'    : [],
    'Fecha' : []
}
if (pagina.status_code == requests.codes.ok):
        #print("La url Existe")
        bs = BeautifulSoup(pagina.text, 'lxml')
        #print(bs)
        #list_all_tags= bs.findAll("td", class_="td1")
        list_all_autores= bs.findAll("td", class_="td1", width="20%")
        for n in range (len(list_all_autores)):
            datos['Autor'].append(list_all_autores[n].text)
            print (list_all_autores[n].text)
        #list_all_titulos= bs.findAll("td", class_="td1", width="40%")
        #print(list_all_titulos)

        links =[]
        for tag in bs.find_all("td", class_="td1", width="40%"):
                for anchor in tag.find_all("a"):
                    links.append(anchor["a.text"])

        #print(list_all_titulos)
        print (links)
else:
        print("No ta la wea")
