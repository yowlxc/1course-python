import os
from urllib.parse import urlparse, parse_qs
from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

from models.author import Author
from controllers.databasecontroller import DatabaseController

# === Jinja2 ===
template_dir = os.path.join(os.path.dirname(__file__), "templates")
env = Environment(
    loader=FileSystemLoader(template_dir),
    autoescape=select_autoescape(['html', 'xml'])
)

# === Глобальные данные ===
main_author = Author('Nastya Pirogova', 'P3121')
db = DatabaseController()  # ← Создаём БД при старте


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        try:
            if path == '/':
                # Главная страница — список валют
                currencies = db.get_all_currencies()
                template = env.get_template("index.html")
                result = template.render(
                    myapp="Currency Tracker",
                    navigation=[
                        {'caption': 'Основная страница', 'href': '/'},
                        {'caption': 'Пользователи', 'href': '/users'},
                        {'caption': 'Курсы валют', 'href': '/currencies'},
                        {'caption': 'Об авторе', 'href': '/author'}
                    ],
                    author_name=main_author.name,
                    author_group=main_author.group,
                    currencies=currencies
                )

            elif path == '/users':
                # Страница со списком пользователей
                users = db.get_all_users()
                template = env.get_template("users.html")
                result = template.render(
                    users=users,
                    navigation=[
                        {'caption': 'Основная страница', 'href': '/'},
                        {'caption': 'Об авторе', 'href': '/author'}
                    ]
                )

            elif path == '/currencies':
                # Отдельная страница валют (можно использовать тот же index.html)
                currencies = db.get_all_currencies()
                template = env.get_template("currencies.html")  # или "index.html"
                result = template.render(
                    currencies=currencies,
                    navigation=[...]
                )

            elif path == '/user':
                # Страница конкретного пользователя (с ?id=...)
                user_id = query.get('id', [None])[0]
                if user_id and user_id.isdigit():
                    user_id = int(user_id)
                    user = db.get_user_by_id(user_id)
                    if user:
                        subscriptions = db.get_user_subscriptions(user_id)
                        template = env.get_template("user.html")
                        result = template.render(
                            user=user,
                            currencies=subscriptions,
                            navigation=[
                                {'caption': 'Основная страница', 'href': '/'},
                                {'caption': 'Пользователи', 'href': '/users'},
                                {'caption': 'Об авторе', 'href': '/author'}
                            ]
                        )
                    else:
                        result = "<h1>Пользователь не найден</h1>"
                else:
                    result = "<h1>Не указан ID пользователя</h1>"

            elif path == '/author':
                template = env.get_template("author.html")
                result = template.render(
                    author=main_author,
                    app={'version': '1.0'},
                    navigation=[...]
                )

            elif path == '/currency/delete':
                currency_id = query.get('id', [None])[0]
                if currency_id and currency_id.isdigit():
                    db.delete_currency(int(currency_id))
                self.send_response(302)
                self.send_header('Location', '/currencies')
                self.end_headers()
                return

            elif path == '/currency/delete':
                currency_id = query.get('id', [None])[0]
                if currency_id and currency_id.isdigit():
                    db.delete_currency(int(currency_id))
                self.send_response(302)
                self.send_header('Location', '/currencies')
                self.end_headers()
                return

            elif path == '/currency/update':
                currency_id = query.get('id', [None])[0]
                new_value = query.get('value', [None])[0]
                if currency_id and currency_id.isdigit() and new_value:
                    try:
                        db.update_currency_value(int(currency_id), float(new_value))
                    except ValueError:
                        pass  # игнорируем некорректное значение
                self.send_response(302)
                self.send_header('Location', '/currencies')
                self.end_headers()
                return

            elif path == '/currencies/update_all':
                # Обновляем все курсы из API
                from utils.currencies_api import get_currencies
                raw_currencies = get_currencies()  # получаем словарь {'USD': 77.5, ...}

                # Получаем все валюты из БД
                currencies = db.get_all_currencies()
                for curr in currencies:
                    char_code = curr['char_code']
                    if char_code in raw_currencies:
                        db.update_currency_value(curr['id'], raw_currencies[char_code])

                self.send_response(302)
                self.send_header('Location', '/currencies')
                self.end_headers()
                return
            
            elif path == '/currency/update_from_api':
                currency_id = query.get('id', [None])[0]
                if currency_id and currency_id.isdigit():
                    # Получаем валюту из БД, чтобы узнать char_code
                    currency = db.get_currency_by_id(int(currency_id))
                    if currency:
                        from utils.currencies_api import get_currencies
                        api_data = get_currencies()  # словарь: {'USD': 77.5, ...}
                        char_code = currency['char_code']
                        if char_code in api_data:
                            new_value = api_data[char_code]
                            db.update_currency_value(int(currency_id), new_value)
                self.send_response(302)
                self.send_header('Location', '/currencies')
                self.end_headers()
                return

            else:
                result = "<h1>404 — Страница не найдена</h1>"

            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(result.encode('utf-8'))

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"<h1>Ошибка: {e}</h1>".encode('utf-8'))


if __name__ == "__main__":
    print("Сервер запущен на http://localhost:8080")
    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
        db.close()