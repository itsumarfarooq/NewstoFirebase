import requests
from parsel import Selector
import json
from firebase import Firebase
import datetime

def get_breitbart_headlines():
    url = "https://www.breitbart.com/"

    headers = {
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document'
    }
    response = requests.get(url, headers=headers)
    sel = Selector(response.text)
    headlines = []
    texts_to_ignore = ['{{icon}}{{headline}}', 'Have a news tip?']
    for headline_elem in sel.xpath('//section[@id="MainW"]//a[parent::h2]'):
        headline = {}
        headline['text'] = headline_elem.xpath('string(.)').get('').strip()
        if headline['text']:
            headline['url'] = headline_elem.xpath('./@href').get()
        headline['source'] = 'breitbart.com'
        headline['datetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        headlines.append(headline)
    return headlines

if __name__ == '__main__':
    config =  {
        'apiKey': "AIzaSyA-gwShYTSeDiroeDewu7PV9piKVslDAAQ",
        'authDomain': "headlines-9ced6.firebaseapp.com",
        'databaseURL': "https://headlines-9ced6.firebaseio.com",
        'storageBucket': "headlines-9ced6.appspot.com",
        "serviceAccount": "credentials.json"
    }

    firebase = Firebase(config)
    db = firebase.database()
    db.push(get_breitbart_headlines())