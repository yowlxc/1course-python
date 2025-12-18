from jinja2 import Environment, PackageLoader, select_autoescape
from models import Author, User

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from utils.currencies_api import get_currencies

navigation =[{'caption': 'Основная страница',
                                   'href': "/" },
                                   {'caption': 'Авторизация',
                                    'href': "/autorization"},
                                   {'caption': 'Пользователи',
                                    'href': "/users"},
                                   {'caption': 'Выход',
                                    'href': "/logout"},
                                    {'caption': 'Яндекс',
                                    'href': "https://google.com"},
                                   {'caption': 'Курсы валют',
                                    'href': "/courses"}]

users = [User(1, 'Nastya'), User(2, 'Vladimir')]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Вызвана страница: " + self.path)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()

        if self.path == '/users':
            result = users_template.render(users = users, navigation = navigation)
        elif self.path == '/courses':
            courses = get_currencies(['USD', 'BYN', 'EUR'])
            for key, value in courses.items():
                print(f"Ключ: {key}, Значение: {value}") 
            result = courses_template.render(courses = courses, navigation = navigation)
        else:
            result = template.render(myapp="CurrenciesListApp",
                            navigation = navigation,
                        author_name = main_author.name,
                        group = main_author.group
                        )
        self.wfile.write(bytes(result, "utf-8"))


env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape()
)

template = env.get_template("index.html")
users_template = env.get_template("users.html")
courses_template = env.get_template("courses.html")

main_author = Author('Nastya','P3121')

httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
print('server is running')
httpd.serve_forever()


# http://127.0.0.1:8080/