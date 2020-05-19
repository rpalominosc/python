import requests
from bs4 import BeautifulSoup
from lxml import html

USERNAME = "81534675"
PASSWORD = "polux7leo"

LOGIN_URL = "https://zeusr.sii.cl//AUT2000/InicioAutenticacion/IngresoRutClave.html?https://misiir.sii.cl/cgi_misii/siihome.cgi"
URL = "http://www.sii.cl/servicios_online/1040-1287.html#-collapseOne"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    #authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "rutcntr": USERNAME,
        "clave": PASSWORD
        #"csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    pagina=  requests.get(URL)
    if (pagina.status_code == requests.codes.ok):
        print("It's OK!!!")
        bs = BeautifulSoup(pagina.text, 'lxml')
    else:
        print("not OK")
    print(bs)
    bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    print(bucket_names)

if __name__ == '__main__':
    main()
