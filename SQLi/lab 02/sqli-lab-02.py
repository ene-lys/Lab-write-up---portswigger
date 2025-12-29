import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1"8080'}

def get_csrf_token(s, url):
    r = s.get(url, verify = False, proxies = proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input")['value']
    print(csrf)

def exploit(s, url, payload):
    csrf = get_csrf_token(s, url)
    #does nothing

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print(f'[-] Usage {sys.argv[0]} <url> <payload>')
        print(f'[-] Example {sys.argv[0]} example.com "1=1"')

    s = requests.Session()
    #Cookie to be the same
    #Data to be passes along

    if exploit(s, url, payload):
        print('[+] SQL injection successful! We have logged in as the administrator user')
    else:
        print('[-] SQL injection unsuccessful')