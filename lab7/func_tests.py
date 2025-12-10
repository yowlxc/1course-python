import unittest
from get_currencies import get_currencies
from unittest.mock import patch, Mock

class TestGetCurrencies(unittest.TestCase):

    def test_CorrectData (self):
        res = get_currencies({'USD', 'BYN'})
        self.assertIn('BYN', res)     
        self.assertIsInstance(res['BYN'], (float))
        self.assertIn('USD', res) 
        self.assertIsInstance(res['USD'], (float))

    def test_ValuteNotExist (self):
        res = get_currencies({'USD', 'BYN','XYZ'})
        self.assertIn('BYN', res)     
        self.assertIsInstance(res['BYN'], (float))
        self.assertIn('USD', res) 
        self.assertIsInstance(res['USD'], (float))   
        self.assertIn('XYZ', res) 
        self.assertIsInstance(res['XYZ'], (str))  

    def test_ConnectionError(self):
        with self.assertRaises(ConnectionError):
            get_currencies(['USD'], url="https://invalid-url")   

    def test_InvalidJson(self):
        with self.assertRaises(ValueError) as cm:
            get_currencies(['USD'], url="https://example.com")
        self.assertIn("Некорректный JSON", str(cm.exception))

    def test_KeyError(self):
        mock_response = Mock()
        mock_response.raise_for_status = lambda: None
        mock_response.json.return_value = {"SomeOtherKey": 123} 

        with patch('get_currencies.requests.get', return_value=mock_response):
            with self.assertRaises(KeyError) as cm:
                get_currencies(["USD"])
            self.assertEqual(cm.exception.args[0], "Нет ключа Valute")

if __name__ == '__main__':
    unittest.main()