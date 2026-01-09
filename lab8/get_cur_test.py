# test_app.py
from requests.exceptions import RequestException
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'utils'))
sys.path.insert(0, os.path.dirname(__file__))

from utils.currencies_api import get_currencies

class TestGetCurrencies(unittest.TestCase):

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "Valute": {
                "USD": {"Value": 75.5},
                "EUR": {"Value": 80.1}
            }
        }
        mock_get.return_value = mock_response

        result = get_currencies()
        self.assertEqual(result["USD"], 75.5)
        self.assertEqual(result["EUR"], 80.1)

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_no_valute_key(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"Other": "data"}
        mock_get.return_value = mock_response

        with self.assertRaises(KeyError):
            get_currencies()

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_invalid_json(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.side_effect = ValueError("No JSON")
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError):
            get_currencies()

    @patch('utils.currencies_api.requests.get')
    def test_get_currencies_network_error(self, mock_get):
        mock_get.side_effect = RequestException("Connection failed")

        with self.assertRaises(ConnectionError):
            get_currencies()

if __name__ == "__main__":
    unittest.main(verbosity=2)