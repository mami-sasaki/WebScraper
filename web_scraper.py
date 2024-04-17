import json
import requests
from functools import lru_cache
from flask import Flask, jsonify, request

app = Flask(__name__) 

CONTENTS = 'contents'
MAIN_CONTENT = 'mainContent'
RECORDS = 'records'
ATTRIBUTES = 'attributes'
PRODUCT_DISPLAYNAME = 'product.displayName'

results = []

class WebScraper():
    def __init__(self):
        pass


    def create_response(self, url, data):
        display_name = None
        try:
            return data[CONTENTS][0][MAIN_CONTENT][0][CONTENTS][0][RECORDS][0][ATTRIBUTES][PRODUCT_DISPLAYNAME]
        except KeyError as e:
            missing_key = str(e).split("'")[1]
            return {'url': url, 'error': f'{missing_key} key is missing'}


    @lru_cache(maxsize=128)
    def extract_product_details(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                json_data = response.json()
                return self.create_response(url, json_data) 
            else:
                return {'url': url, 'error': f'Failed to fetch data. Status code: {response.status_code}'}
        except Exception as e:
            return {'url': url, 'error': f'An error occured: {str(e)}'}
 
 
@app.route('/product-details', methods=['GET'])
def read_data():
    global results
    data = request.json
    if isinstance(data, list):
        web_scraper = WebScraper()
        for url in data:
            display_name = web_scraper.extract_product_details(url)
            product_dict = {'url': url, 'displayName': display_name}
            if product_dict not in results:
                results.append(product_dict)
        res = jsonify(results), 200
    else:
        res = jsonify({'error': 'Invalid data format. List of URLs expected.'}), 400
    return res
        

if __name__ == "__main__":
    app.run(port=5000)

