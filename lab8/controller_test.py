# controller_test.py
import unittest
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import sys

# Добавляем путь к моделям и утилитам
sys.path.insert(0, os.path.dirname(__file__))

from myapp import users, user_currencies, navigation, main_author, get_currencies, Currency
from models import User


class TestController(unittest.TestCase):

    def setUp(self):
        # Настраиваем Jinja2, как в myapp.py
        template_dir = os.path.join(os.path.dirname(__file__), "templates")
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def test_route_index(self):
        template = self.env.get_template("index.html")
        html = template.render(
            author_name=main_author.name,
            group=main_author.group,
            navigation=navigation
        )
        self.assertIn("Currency Tracker", html)
        self.assertIn("Nastya Pirogova", html)

    def test_route_users(self):
        template = self.env.get_template("users.html")
        html = template.render(users=users, navigation=navigation)
        self.assertIn("Nastya Pirogova", html)
        self.assertIn("Vladimir Pirogov", html)

    def test_route_courses(self):
        # Эмулируем получение курсов
        raw_currencies = {"USD": 75.5, "EUR": 80.1}
        currencies = []
        for char_code, value in raw_currencies.items():
            if isinstance(value, (int, float)):
                currencies.append(Currency(
                    num_code=0,
                    char_code=char_code,
                    name=f"Валюта {char_code}",
                    value=value,
                    nominal=1.0
                ))
        template = self.env.get_template("courses.html")
        html = template.render(currencies=currencies, navigation=navigation)
        self.assertIn("USD", html)
        self.assertIn("75.5", html)

    def test_route_user(self):
        user = users[0]  # Nastya Pirogova, id=1
        subs = [uc for uc in user_currencies if uc.user_id == user.id]
        raw_currencies = {"USD": 75.5, "EUR": 80.1}
        currencies = []
        for sub in subs:
            code = sub.currency_id
            if code in raw_currencies:
                currencies.append(Currency(
                    num_code=0,
                    char_code=code,
                    name=f"Валюта {code}",
                    value=raw_currencies[code],
                    nominal=1.0
                ))
        template = self.env.get_template("user.html")
        html = template.render(user=user, currencies=currencies, navigation=navigation)
        self.assertIn("Nastya Pirogova", html)
        self.assertIn("USD", html)

if __name__ == "__main__":
    unittest.main(verbosity=2)