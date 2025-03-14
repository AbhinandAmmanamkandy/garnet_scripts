import requests
import urllib.request
from bs4 import BeautifulSoup

# Get latest release version number
def get_version(url):
    url = url + "/releases/latest"
    response = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(response.text, "html.parser")
    return "v" + soup.title.string.split("v", 1)[-1].split()[0]

# Get all released apk links
def get_apk_links(url):
    response = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(response.text, "html.parser")
    return [f"https://github.com{a.get("href")}" for a in soup.find_all("a", href=True) if a["href"].endswith(".apk")]

# Basic download
def download_file(link, name):
    urllib.request.urlretrieve(link, name)

# Ask the user which to download
def get_latest_release(url):
    version = get_version(url)

    url = f"{url}/releases/expanded_assets/{version}"
    apk_links = get_apk_links(url)
    apks = [link.split('/')[-1] for link in apk_links]

    for i, name in enumerate(apks, 1):
        print(f"{i}. {name}")

    choice = int(input("Enter choice: ")) - 1
    download_file(apk_links[choice], apks[choice])