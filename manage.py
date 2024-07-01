from bs4 import BeautifulSoup
import requests
from config.baseScraper import BaseScraper
from config.DatasetScraper import DatasetScraper


def main():
    url = "https://catalog.data.gov/dataset"
    scraper = DatasetScraper()
    collection = scraper.scraper(url)
    print(collection)

if __name__ == '__main__':
    main()
