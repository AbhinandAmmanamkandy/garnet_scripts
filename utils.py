import requests
from bs4 import BeautifulSoup

def get_version(url):
    response = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(response.text, "html.parser")
    return "v" + soup.title.string.split("v", 1)[-1].split()[0]

def get_apk_links(url):
    response = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(response.text, "html.parser")
    return [f"https://github.com{a.get("href")}" for a in soup.find_all("a", href=True) if a["href"].endswith(".apk")]