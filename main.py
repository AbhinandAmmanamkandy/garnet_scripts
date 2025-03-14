import requests
import urllib.request
from bs4 import BeautifulSoup

base_url = "https://github.com"
sub_url = "tiann/KernelSU"
url = f"{base_url}/{sub_url}/releases/latest"

response = requests.get(url, allow_redirects=True)
soup = BeautifulSoup(response.text, "html.parser")

version = "v" + soup.title.string.split("v", 1)[-1].split()[0]

url = f"{base_url}/{sub_url}/releases/expanded_assets/{version}"
response = requests.get(url, allow_redirects=True)

soup = BeautifulSoup(response.text, "html.parser")
apk_links = [f"{base_url}{a.get("href")}" for a in soup.find_all("a", href=True) if a["href"].endswith(".apk")]
apks = [link.split('/')[-1] for link in apk_links]

for i, name in enumerate(apks, 1):
    print(f"{i}. {name}")

choice = int(input("Enter choice: ")) - 1
urllib.request.urlretrieve(apk_links[choice], apks[choice])