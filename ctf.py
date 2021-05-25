import requests
import json

from bs4 import BeautifulSoup


url = "https://ctftime.org/event/list/upcoming"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/4.0 (Windows NT 7.0; Win86; x86; rv:82.0) Gecko/201110101 Firefox/77.0"
}

req = requests.get(url, headers=headers)

soup = BeautifulSoup(req.text, 'lxml')

all_ctfs = soup.find('table', class_="table").find_all('a')


all_ctfs_dict = {}
for ctf in all_ctfs:
    ctf_name = ctf.text
    ctf_link = f"https://ctftime.org{ctf.get('href')}"
    # print(f"{ctf_name} | {ctf_link}")

    all_ctfs_dict[ctf_name] = ctf_link


with open("all_ctfs.json", "w") as file:
    json.dump(all_ctfs_dict, file, indent=4, ensure_ascii=False)
