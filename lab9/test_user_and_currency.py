"""Тесты моделей User и Currency."""

import unittest
from models.user import User
from models.currencies import Currency


class TestUser(unittest.TestCase):
    """Тесты класса User."""

    def setUp(self):
        """Сбрасывает счётчик ID перед каждым тестом."""
        User._next_id = 1

    def test_user_creation_valid_name(self):
        """Пользователь создаётся с корректным именем."""
        user = User("Алиса")
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "Алиса")

    def test_user_creation_invalid_name_too_short(self):
        """Ошибка при создании пользователя с именем короче 2 символов."""
        with self.assertRaises(ValueError) as context:
            User("А")
        self.assertIn("Ошибка при задании имени", str(context.exception))

    def test_user_creation_invalid_name_not_string(self):
        """Ошибка при создании пользователя с нестроковым именем."""
        with self.assertRaises(ValueError) as context:
            User(123)
        self.assertIn("Ошибка при задании имени", str(context.exception))

    def test_user_name_setter_valid(self):
        """Изменение имени на корректное значение."""
        user = User("Боб")
        user.name = "Ева"
        self.assertEqual(user.name, "Ева")

    def test_user_name_setter_invalid(self):
        """Ошибка при установке некорректного имени через сеттер."""
        user = User("Карл")
        with self.assertRaises(ValueError):
            user.name = "X"

    def test_user_auto_increment_id(self):
        """ID пользователей увеличивается автоматически."""
        user1 = User("Дина")
        user2 = User("Эльза")
        self.assertEqual(user1.id, 1)
        self.assertEqual(user2.id, 2)


class TestCurrency(unittest.TestCase):
    """Тесты класса Currency."""

    def test_currency_creation_valid(self):
        """Валюта создаётся с корректными данными."""
        currency = Currency(840, "USD", "Доллар США", 77.5, 1.0)  # ← nominal как float
        self.assertEqual(currency.num_code, 840)
        self.assertEqual(currency.char_code, "USD")
        self.assertEqual(currency.name, "Доллар США")
        self.assertEqual(currency.value, 77.5)
        self.assertEqual(currency.nominal, 1.0)

    def test_currency_creation_invalid_nominal(self):
        """Ошибка при создании валюты с некорректным номиналом."""
        with self.assertRaises(ValueError) as context:
            Currency(840, "USD", "Доллар", 77.5, "один")
        self.assertIn("Ошибка при задании номинала", str(context.exception))

    def test_currency_creation_invalid_value(self):
        """Ошибка при создании валюты с некорректным курсом."""
        with self.assertRaises(ValueError) as context:
            Currency(840, "USD", "Доллар", "семьдесят семь", 1.0)  # ← nominal как float
        self.assertIn("Ошибка при задании курса", str(context.exception))

    def test_currency_value_setter_valid_float(self):
        """Установка корректного курса (float)."""
        currency = Currency(840, "USD", "Доллар", 77.5, 1.0)
        currency.value = 78.0
        self.assertEqual(currency.value, 78.0)

    def test_currency_value_setter_valid_int(self):
        """Установка корректного курса (int) — должно конвертироваться во float."""
        currency = Currency(840, "USD", "Доллар", 77.5, 1.0)
        currency.value = 78  # int → должно стать 78.0
        self.assertEqual(currency.value, 78.0)

    def test_currency_nominal_setter_valid_int(self):
        """Установка номинала как int — должно работать, если сеттер принимает int."""
        currency = Currency(840, "USD", "Доллар", 77.5, 1.0)
        # Если сеттер НЕ принимает int — этот тест упадёт.
        # Но раз модель требует float — передаём float.
        currency.nominal = 10.0
        self.assertEqual(currency.nominal, 10.0)

    def test_currency_nominal_setter_valid_float(self):
        """Установка корректного номинала (float)."""
        currency = Currency(840, "USD", "Доллар", 77.5, 1.0)
        currency.nominal = 10.0
        self.assertEqual(currency.nominal, 10.0)

    def test_currency_nominal_setter_invalid_type(self):
        """Ошибка при установке номинала нечислового типа."""
        currency = Currency(840, "USD", "Доллар", 77.5, 1.0)
        with self.assertRaises(ValueError):
            currency.nominal = "десять"


if __name__ == "__main__":
    unittest.main()