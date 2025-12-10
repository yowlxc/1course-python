import unittest
import io
import logging
from my_logger import logger
from get_currencies import get_currencies
from unittest.mock import patch, Mock


class TestDecoratorLogging(unittest.TestCase):

    def setUp(self):
        self.stream = io.StringIO()

        @logger(handle=self.stream)
        def wrapped_get_currencies(currency_codes, url=None):
            if url:
                return get_currencies(currency_codes, url)
            return get_currencies(currency_codes)

        self.wrapped = wrapped_get_currencies

    #Проверка логирования успешного вызова через StringIO
    def test_SuccessTry(self):
        result = self.wrapped(['USD'])
        self.assertRegex(self.stream.getvalue(), "INFO")
        self.assertRegex(self.stream.getvalue(), "Функция wrapped_get_currencies завершена успешно. Результат: ")
        self.assertRegex(self.stream.getvalue(), "Вызов функции wrapped_get_currencies")
        self.assertIn("USD", str(result))
        self.assertIsInstance(result['USD'], float)

    #Проверка логирования ConnectionError через декоратор
    def test_ConnectionError(self):
        with self.assertRaises(ConnectionError):
            self.wrapped(['USD'], url="https://invalid-url") 

        self.assertRegex(self.stream.getvalue(), "ERROR")
        self.assertRegex(self.stream.getvalue(), "ConnectionError")
        self.assertRegex(self.stream.getvalue(), "API недоступен")

    #Проверка логирования KeyError через декоратор
    def test_KeyError(self):
        mock_response = Mock()
        mock_response.raise_for_status = lambda: None
        mock_response.json.return_value = {"SomeOtherKey": 123} 

        with patch('get_currencies.requests.get', return_value=mock_response):
            with self.assertRaises(KeyError) as cm:
                self.wrapped(["USD"])

        self.assertRegex(self.stream.getvalue(), "ERROR")
        self.assertRegex(self.stream.getvalue(), "KeyError")

if __name__ == "__main__":
    unittest.main(verbosity=2)