"""Основной модуль веб-сервера для отображения курсов валют и управления подписками."""

import os
from urllib.parse import urlparse, parse_qs
from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

from models.author import Author
from controllers.databasecontroller import DatabaseController


# Настройка шаблонизатора Jinja2
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")
ENV = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    autoescape=select_autoescape(["html", "xml"])
)

# Глобальные данные приложения
MAIN_AUTHOR = Author("Nastya Pirogova", "P3121")
DB = DatabaseController()


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Обработчик HTTP-запросов для веб-интерфейса."""

    def do_GET(self) -> None:
        """Обрабатывает GET-запросы к различным маршрутам приложения."""
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        try:
            if path == "/":
                # Главная страница — список валют
                currencies = DB.get_all_currencies()
                template = ENV.get_template("index.html")
                result = template.render(
                    myapp="Currency Tracker",
                    navigation=[
                        {"caption": "Основная страница", "href": "/"},
                        {"caption": "Пользователи", "href": "/users"},
                        {"caption": "Курсы валют", "href": "/currencies"},
                        {"caption": "Об авторе", "href": "/author"},
                    ],
                    author_name=MAIN_AUTHOR.name,
                    author_group=MAIN_AUTHOR.group,
                    currencies=currencies,
                )

            elif path == "/users":
                # Страница со списком пользователей
                users = DB.get_all_users()
                template = ENV.get_template("users.html")
                result = template.render(
                    users=users,
                    navigation=[
                        {"caption": "Основная страница", "href": "/"},
                        {"caption": "Об авторе", "href": "/author"},
                    ],
                )

            elif path == "/currencies":
                # Страница со списком валют
                currencies = DB.get_all_currencies()
                template = ENV.get_template("currencies.html")
                result = template.render(currencies=currencies)

            elif path == "/user":
                # Страница конкретного пользователя
                user_id = query.get("id", [None])[0]
                if user_id and user_id.isdigit():
                    user_id = int(user_id)
                    user = DB.get_user_by_id(user_id)
                    if user:
                        subscriptions = DB.get_user_subscriptions(user_id)
                        template = ENV.get_template("user.html")
                        result = template.render(
                            user=user,
                            currencies=subscriptions,
                            navigation=[
                                {"caption": "Основная страница", "href": "/"},
                                {"caption": "Пользователи", "href": "/users"},
                                {"caption": "Об авторе", "href": "/author"},
                            ],
                        )
                    else:
                        result = "<h1>Пользователь не найден</h1>"
                else:
                    result = "<h1>Не указан ID пользователя</h1>"

            elif path == "/author":
                # Страница информации об авторе
                template = ENV.get_template("author.html")
                result = template.render(
                    author=MAIN_AUTHOR,
                    app={"version": "1.0"},
                )

            elif path == "/currency/delete":
                # Удаление валюты
                currency_id = query.get("id", [None])[0]
                if currency_id and currency_id.isdigit():
                    DB.delete_currency(int(currency_id))
                self.send_response(302)
                self.send_header("Location", "/currencies")
                self.end_headers()
                return

            elif path == "/currencies/update_all":
                # Обновление всех курсов из API ЦБ РФ
                from utils.currencies_api import get_currencies

                raw_currencies = get_currencies()
                currencies = DB.get_all_currencies()
                for curr in currencies:
                    char_code = curr["char_code"]
                    if char_code in raw_currencies:
                        DB.update_currency_value(curr["id"], raw_currencies[char_code])
                self.send_response(302)
                self.send_header("Location", "/currencies")
                self.end_headers()
                return

            elif path == "/currency/update_from_api":
                # Обновление курса конкретной валюты из API
                currency_id = query.get("id", [None])[0]
                if currency_id and currency_id.isdigit():
                    currency = DB.get_currency_by_id(int(currency_id))
                    if currency:
                        from utils.currencies_api import get_currencies

                        api_data = get_currencies()
                        char_code = currency["char_code"]
                        if char_code in api_data:
                            new_value = api_data[char_code]
                            DB.update_currency_value(int(currency_id), new_value)
                self.send_response(302)
                self.send_header("Location", "/currencies")
                self.end_headers()
                return

            else:
                result = "<h1>404 — Страница не найдена</h1>"

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(result.encode("utf-8"))

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"<h1>Ошибка: {e}</h1>".encode("utf-8"))


if __name__ == "__main__":
    print("Сервер запущен на http://localhost:8080")
    httpd = HTTPServer(("localhost", 8080), SimpleHTTPRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
        DB.close()