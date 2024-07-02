from bs4 import BeautifulSoup
import requests
from config.baseScraper import BaseScraper
from config.DatasetScraper import DatasetScraper


def main():
    url = "https://catalog.data.gov/dataset"
    scraper = DatasetScraper()
    collection = scraper.scraper(url)
    
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Information</title>
    </head>
    <body>
        <h1>User Information</h1>
    """
    
    
        
    for dataset, view in zip(collection['dataset'], collection['view']):
        html_content += f"""
        <span>{dataset} - {view}</span><br>
        """
    
    html_content += """
    </body>
    </html>
    """

    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
        file.close()

if __name__ == '__main__':
    main()
