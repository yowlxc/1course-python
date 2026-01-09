"""Тесты для модуля currencies_api."""

import unittest
from unittest.mock import patch, MagicMock
from utils.currencies_api import get_currencies


class TestGetCurrencies(unittest.TestCase):
    """Тесты функции get_currencies."""

    @patch("utils.currencies_api.requests.get")
    def test_get_currencies_success(self, mock_get):
        """Успешное получение курсов."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "Valute": {
                "USD": {"Value": 77.5},
                "EUR": {"Value": 90.34}
            }
        }
        mock_get.return_value = mock_response

        result = get_currencies(["USD", "EUR"])
        self.assertEqual(result["USD"], 77.5)
        self.assertEqual(result["EUR"], 90.34)

    @patch("utils.currencies_api.requests.get")
    def test_get_currencies_network_error(self, mock_get):
        """Обработка ошибки сети."""
        from requests.exceptions import ConnectionError as RequestsConnectionError
        mock_get.side_effect = RequestsConnectionError("Network down")

        with self.assertRaises(ConnectionError):
            get_currencies()

    @patch("utils.currencies_api.requests.get")
    def test_get_currencies_invalid_json(self, mock_get):
        """Обработка некорректного JSON."""
        mock_response = MagicMock()
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError):
            get_currencies()

if __name__ == "__main__":
    unittest.main(verbosity=2)