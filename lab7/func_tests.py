import unittest
from get_currencies import get_currencies

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

    def test_invalid_json(self):
        with self.assertRaises(ValueError) as cm:
            get_currencies(['USD'], url="https://example.com")
        self.assertIn("Некорректный JSON", str(cm.exception))

    def test_KeyError(self):
        with self.assertRaises(ConnectionError):
            get_currencies(['USD'], url="https://invalid-url") 


if __name__ == '__main__':
    unittest.main()