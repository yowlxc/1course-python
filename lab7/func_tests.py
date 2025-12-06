import unittest
from get_currencies import get_currencies

class TestGetCurrencies(unittest.TestCase):

    def test_CorrectData (self):
        res = get_currencies({'USD', 'BYN'})
        self.assertIn('BYN', res)     
        self.assertIsInstance(res['BYN'], (float))
        self.assertIn('USD', res) 
        self.assertIsInstance(res['USD'], (float))

    # def test_ValuteNotExist (self):
    #     self.assertEqual(get_currencies({'USD', 'BYN','XYZ'}), {'USD': 76.0937, 'XYZ': "Код валюты 'XYZ' не найден", 'BYN': 26.4517})       

if __name__ == '__main__':
    unittest.main()