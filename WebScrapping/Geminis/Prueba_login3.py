import requests
from bs4 import BeautifulSoup
from lxml import html

USERNAME = "023604-S"
PASSWORD = "Polux9leo."

LOGIN_URL = "http://geminis.si2.cl:8020/auth/login"
URL = "http://geminis.si2.cl:8080/#/indices"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    print(result)
    tree = html.fromstring(result.text)
    print(tree)
    #authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME,
        "password": PASSWORD
        #"csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    #result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
    result = requests.get("http://geminis.si2.cl:8020/auth/login", auth=('USERNAME', 'PASSWORD'))
    print(result.url)
    print(result.status_code)
    print(result.history)
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
