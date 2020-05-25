import requests
import requests.auth
import urllib
from bs4 import BeautifulSoup
from lxml import html
from oauthlib.oauth2 import LegacyApplicationClient
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

USERNAME = "023604-S"
PASSWORD = "Polux9leo."
client_id = 'SampleClientId'
client_secret = 'secret'

authorize_url = 'http://geminis.si2.cl:8020/auth/oauth/authorize'
token_url = 'http://geminis.si2.cl:8020/auth/oauth/token '
LOGIN_URL = "http://geminis.si2.cl:8020/auth/login"
URL_LLAMADA = "http://geminis.si2.cl:8080/#/indices"

def main():
    session_requests = requests.session()

    # Obtencion  login csrf token
    oauth = OAuth2Session(client = LegacyApplicationClient(client_id=client_id))
    token = oauth.fetch_token(token_url='http://geminis.si2.cl:8020/auth/oauth/token', username=USERNAME, password=PASSWORD, client_id=client_id,client_secret=client_secret)
    result = session_requests.get(URL_LLAMADA)
    print(result)

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
