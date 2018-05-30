import requests
from bs4 import BeautifulSoup

s = requests.Session()
r = s.get("https://110.49.11.34/login",verify=False)
soup = BeautifulSoup(r.content, "html.parser")
print(soup)
print(r.headers)
data = soup.find_all("span", {"itemprop": "price"})
print(data)
