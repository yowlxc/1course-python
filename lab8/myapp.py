import os
import sys
from urllib.parse import urlparse, parse_qs
from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models import Author, App, User, Currency, UserCurrency
from utils.currencies_api import get_currencies

# === Глобальные данные ===
main_author = Author('Nastya Pirogova', 'P3121')
main_app = App(name="Currency Tracker", version="1.0", author=main_author)

users = [
    User('Nastya Pirogova'),
    User('Vladimir Pirogov'),
    User('Natasha Karpova'),
    User('Vika Vodovozova'),
]

user_currencies = [
    UserCurrency(id=1, user_id=1, currency_id="USD"),  
    UserCurrency(id=2, user_id=1, currency_id="EUR"),
    UserCurrency(id=3, user_id=2, currency_id="EUR"),
]

navigation = [
    {'caption': 'Основная страница', 'href': '/'},
    {'caption': 'Пользователи', 'href': '/users'},
    {'caption': 'Курсы валют', 'href': '/courses'},
]

template_dir = os.path.join(os.path.dirname(__file__), "templates")
env = Environment(
    loader=FileSystemLoader(template_dir),
    autoescape=select_autoescape(['html', 'xml'])
)

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        try:
            if path == '/':
                self._render_index()
            elif path == '/users':
                self._render_users()
            elif path == '/courses':
                # Получаем курсы как словарь
                raw_currencies = get_currencies()  # Теперь работает без аргументов
                
                # Преобразуем в список объектов Currency
                currencies = []
                for char_code, value in raw_currencies.items():
                    if isinstance(value, (int, float)):
                        currencies.append(Currency(
                            id=char_code,
                            num_code=0,          # Заглушка (в JSON-API нет num_code)
                            char_code=char_code,
                            name=f"Валюта {char_code}",
                            value=value,
                            nominal=1
                        ))
                
                self._render_courses(currencies)
            elif path == '/user':
                user_id = query.get('id', [None])[0]
                if user_id is None:
                    self._send_error(400, "Не указан параметр id")
                    return
                try:
                    user_id = int(user_id)
                except ValueError:
                    self._send_error(400, "Некорректный id")
                    return
                user = next((u for u in users if u.id == user_id), None)
                if not user:
                    self._send_error(404, "Пользователь не найден")
                    return
                
                # Найти подписки
                subs = [uc for uc in user_currencies if uc.user_id == user_id]
                user_currency_list = []
                
                # Получаем актуальные курсы для подписок
                raw_currencies = get_currencies()
                for sub in subs:
                    code = sub.currency_id
                    if code in raw_currencies and isinstance(raw_currencies[code], (int, float)):
                        user_currency_list.append(Currency(
                            id=code,
                            num_code=0,
                            char_code=code,
                            name=f"Валюта {code}",
                            value=raw_currencies[code],
                            nominal=1
                        ))
                
                self._render_user(user, user_currency_list) 
            else:
                self._send_error(404, "Страница не найдена")
        except Exception as e:
            self._send_error(500, f"Внутренняя ошибка сервера: {e}")

    def _send_html(self, content: str):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

    def _send_error(self, code: int, message: str):
        self.send_response(code)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(
            f"<html><body><h1>Ошибка {code}</h1><p>{message}</p></body></html>".encode('utf-8')
        )

    def _render_index(self):
        template = env.get_template("index.html")
        html = template.render(
            author_name = main_author.name,
            group = main_author.group,
            navigation=navigation
        )
        self._send_html(html)

    def _render_users(self):
        template = env.get_template("users.html")
        html = template.render(
            users=users,
            navigation=navigation
        )
        self._send_html(html)

    def _render_courses(self, currencies):
        template = env.get_template("courses.html")
        html = template.render(
            currencies=currencies,
            navigation=navigation
        )
        self._send_html(html)

    def _render_user(self, user, currencies):
        template = env.get_template("user.html")
        html = template.render(
            user=user,
            currencies=currencies,
            navigation=navigation
        )
        self._send_html(html)

if __name__ == "__main__":
    port = 8000
    server_address = ("", port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Сервер запущен на http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
        httpd.server_close