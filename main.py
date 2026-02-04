import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/James_Bond"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

link = soup.find("a")

if link and link.get("href"):
    print(link.get("href"))