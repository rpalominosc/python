from  bs4 import BeautifulSoup
import requests, lxml

web = requests.get("https://jupitervidya.com/")

soup = BeautifulSoup(web.content,"lxml")

#print(soup.prettify())
#print(soup.body.text)
for link in soup.find_all("a"):
    print (link)
