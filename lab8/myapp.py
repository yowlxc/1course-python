# / — главная страница с информацией о приложении и авторе
# /users — список пользователей
# /user?id=... — информация о конкретном пользователе и его подписках
# /currencies — список валют с текущими курсами
# /author — информация об авторе
from jinja2 import Environment, PackageLoader, select_autoescape
from models import author

main_author = author.Author('Nastya','P3121')
env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape()
)

template = env.get_template("index.html")

print(template.render(myapp="Приложение для отслеживания курсов валют",
                      navigation =[{'main_page': 'Основная страница',
                                   'href': "https://nastyapir_p3121.ru" },
                                   {'autorization': 'Авторизация',
                                    'href': "https://autorization.ru"},
                                   {'user': 'Пользователь',
                                    'href': "https://user_page.ru"},
                                   {'logout': 'Выход',
                                    'href': "https://logout.ru"},
                                   {'courses': 'Курсы валют',
                                    'href': "https://courses.ru"}],
                      author_name = main_author.name,
                      group = main_author.group
                      ))

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def to_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset = utf-8')
        self.end_headers()
        result = "<html><h1>Hello, world!</h1></html>"
        self.wfile.write(bytes(result, "utf-8"))

httpd = HTTPServer(('localhost, 8080'), HTTPRequestHandler)

if __name__ == "__main__":
    print('server is running')
    httpd.serve_forever()