from  bs4 import BeautifulSoup
import requests, lxml

with open("index.html") as mypage:
    soup = BeautifulSoup(mypage)
    #print(soup)
    #print(soup.prettify())
    print(soup.get_text())
