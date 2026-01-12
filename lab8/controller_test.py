import unittest
import os
import sys

project_root = os.path.dirname(__file__)
sys.path.insert(0, project_root)

from jinja2 import Environment, FileSystemLoader, select_autoescape


class TestController(unittest.TestCase):

    def setUp(self):
        """Инициализирует данные и шаблоны."""
        from myapp import users, user_currencies, navigation, main_author, Currency

        self.users = users
        self.user_currencies = user_currencies
        self.navigation = navigation
        self.main_author = main_author
        self.Currency = Currency

        self.currencies = [
            Currency(num_code=840, char_code="USD", name="Доллар США", value=77.5, nominal=1.0),
            Currency(num_code=978, char_code="EUR", name="Евро", value=90.34, nominal=1.0),
            Currency(num_code=156, char_code="CNY", name="Китайский юань", value=10.96, nominal=10.0),
        ]

        template_dir = os.path.join(project_root, "templates")
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(["html", "xml"])
        )

    def test_route_index(self):
        """Тест главной страницы."""
        template = self.env.get_template("index.html")
        html = template.render(
            myapp="Currency Tracker",
            navigation=self.navigation,
            author_name=self.main_author.name,
            author_group=self.main_author.group,
            currencies=self.currencies
        )
        self.assertIn("Currency Tracker", html)
        self.assertIn(self.main_author.name, html)  

    def test_route_users(self):
        """Тест списка пользователей."""
        template = self.env.get_template("users.html")
        html = template.render(users=self.users, navigation=self.navigation)
        self.assertIn(self.users[0].name, html)

    def test_route_currencies(self):
        """Тест страницы курсов валют."""
        template = self.env.get_template("courses.html")
        html = template.render(currencies=self.currencies, navigation=self.navigation)
        self.assertIn("USD", html)
        self.assertIn("77.5", html)

    def test_route_author(self):
        """Тест страницы об авторе."""
        template = self.env.get_template("author.html")
        html = template.render(
            author_name=self.main_author.name,  # "Nastya Pirogova"
            group=self.main_author.group,       # "P3121"
            app="1.0",
            navigation=self.navigation
        )
        self.assertIn("Nastya Pirogova", html)
        self.assertIn("P3121", html)
        self.assertIn("1.0", html)


if __name__ == "__main__":
    unittest.main(verbosity=2)