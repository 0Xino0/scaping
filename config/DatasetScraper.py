import requests
from bs4 import BeautifulSoup
from config.baseScraper import BaseScraper

class DatasetScraper(BaseScraper):
    def __init__(self):
        super().__init__()

    def scraper(self, url):

        # Get the dataset from the server
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # add dataset to the html file
        with open("dataset.html", "w") as file:
            file.write(soup.prettify())

        # find dataset names and view them saved in dictionary
        dataset = soup.find("div", class_="primary col-md-9 col-xs-12").find_all("h3", class_="dataset-heading")
        collection = dict()
        for value in dataset :
            name = value.find("a").text
            view = value.find("span").text.split(" ")[1]
            # print(view)
            if "dataset" in collection.keys():
                collection["dataset"].append(name)
                collection["view"].append(view)
            else: 
                collection["dataset"] = [name]
                collection["view"] = [view]
        return collection   
     

        
