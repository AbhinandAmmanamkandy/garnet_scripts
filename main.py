import urllib.request
import utils

base_url = "https://github.com"
sub_url = "tiann/KernelSU"
url = f"{base_url}/{sub_url}/releases/latest"

def download_file(link, name):
    urllib.request.urlretrieve(link, name)

version = utils.get_version(url)

url = f"{base_url}/{sub_url}/releases/expanded_assets/{version}"
apk_links = utils.get_apk_links(url)
apks = [link.split('/')[-1] for link in apk_links]

for i, name in enumerate(apks, 1):
    print(f"{i}. {name}")

choice = int(input("Enter choice: ")) - 1
download_file(apk_links[choice], apks[choice])