from bs4 import BeautifulSoup
import requests
import json
from config.baseScraper import BaseScraper
from config.DatasetScraper import DatasetScraper


def main():
    url_xml = "https://sahmeto.com/crypto-sitemap.xml"
    url_dataset = "https://catalog.data.gov/dataset"
    url_stocktwitts = "https://api.stocktwits.com/api/2/streams/suggested.json?filter=top&limit=20&max=579191095"
    scraper = DatasetScraper()
    json_data = scraper.scrape_stocktwitts(url_stocktwitts)
    collection = scraper.scraper(url_dataset)
    coins_list = scraper.scrape_xml(url_xml)

    #collect messages from stocktwits
    messages_object = json_data["messages"]
    messages_collection = [{"message": message["body"]} for message in messages_object]
       
    print(messages_collection)
    
    #create a json file with coin list
    coins_new_list = [{"name": coin} for coin in coins_list]
    coins_json = json.dumps(coins_new_list, indent=4)

    with open('coins.json','w',encoding='utf-8') as file :
        file.write(coins_json)
    
    #create html content and add collection to html file
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>collection Information</title>
    </head>
    <body>
        <h1>collection Information</h1>
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

    #create html content2 and add collection to table in html
    # ایجاد سر صفحه HTML
    html_content2 = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>table collection Information</title>
    </head>
    <body>
        <h1>table collection Information</h1>
        <table border="1">
            <tr>
                <th>dataset</th>
                <th>view</th>
            </tr>
    """

    # افزودن داده‌ها به جدول با استفاده از حلقه for
    for dataset, view in zip(collection['dataset'], collection['view']):
        html_content2 += f"""
            <tr>
                <td>{dataset}</td>
                <td>{view}</td>
            </tr>
        """

    # پایان HTML
    html_content2 += """
        </table>
    </body>
    </html>
    """

    with open('table.html', 'w', encoding='utf-8') as file:
        file.write(html_content2)
        file.close()

if __name__ == '__main__':
    main()
