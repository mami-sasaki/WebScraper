import unittest
from unittest.mock import patch, MagicMock
from web_scraper import WebScraper
        
url = "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json"

class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.web_scraper = WebScraper()
        self.maxDiff = None


    @patch('requests.get')
    def test_extract_product_details_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'contents': [{'mainContent': [{'contents': [{'records': 
                    [{'attributes': {'product.displayName': ['Wunder Train High-Rise Tight 25"']}}]}]}]}]}
        mock_get.return_value = mock_response
        result = self.web_scraper.extract_product_details(url)
        expected_result = ['Wunder Train High-Rise Tight 25"']
        self.assertEqual(result, expected_result)


    @patch('requests.get')
    def test_extract_product_details_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        result = self.web_scraper.extract_product_details(url)
        self.assertEqual(result, {'url': url, 'error': 'Failed to fetch data. Status code: 404'})


    @patch('requests.get')
    def test_extract_product_details_exception(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200 
        mock_get.return_value = mock_response
        mock_response.json.return_value = {'contents': [{'contents': [{'records': 
                    [{'attributes': {'product.displayName': ['Wunder Train High-Rise Tight 25"']}}]}]}]}
        result = self.web_scraper.extract_product_details(url)
        self.assertEqual(result, {'url': url, 'error': 'mainContent key is missing'})


if __name__ == '__main__':
    unittest.main()

