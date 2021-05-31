import requests
import json

from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        self.request = requests.Session()
        self.request.headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/4.0 (Windows NT 7.0; Win86; x86; rv:82.0) Gecko/201110101 Firefox/77.0"
        }
        self.all_ctfs_dict = {}


    def load_page(self):
        url = "https://ctftime.org/event/list/upcoming"
        req = self.request.get(url=url)
        req.raise_for_status()
        return req.text


    def parse_page(self, text):
        soup = BeautifulSoup(text, "lxml")
        all_ctfs = soup.find("table", class_="table").find_all("a")
        for obj in all_ctfs:
            self.parse_info(obj=obj)
            

    def parse_info(self, obj):
        object_name = obj.text
        object_link = f"https://ctftime.org{obj.get('href')}"

        self.save_to_json(obj_name=object_name, obj_link=object_link)


    def save_to_json(self, obj_name, obj_link):
        self.all_ctfs_dict[obj_name] = obj_link

        with open("all_ctfs.json", "w") as file:
            json.dump(self.all_ctfs_dict, file, indent=4, ensure_ascii=False)


    def run(self):
        text = self.load_page()
        self.parse_page(text=text)


if __name__ == "__main__":
    parser = Parser()
    parser.run() 
