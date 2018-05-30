import requests
from bs4 import BeautifulSoup

s = requests.Session()
r = s.get("https://192.168.2.245/login", verify=False)
soup = BeautifulSoup(r.content, "html.parser")
print(soup)
print(r.headers)
data = soup.find_all("span", {"itemprop": "price"})
print(data)
