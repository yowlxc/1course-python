Отчёт по лабораторной работе №8

1. Цели работы:
   1. Создать простое клиент-серверное приложение на Python без серверных фреймворков.
   2. Освоить работу с HTTPServer и маршрутизацию запросов.
   3. Применять шаблонизатор Jinja2 для отображения данных.
   4. Реализовать модели предметной области (User, Currency, UserCurrency, App, Author) с геттерами и сеттерами.
   5. Структурировать код в соответствии с архитектурой MVC.
   6. Получать данные о курсах валют через функцию get_currencies и отображать их пользователям.
   7. Реализовать функциональность подписки пользователей на валюты и отображение динамики их изменения.
   8. Научиться создавать тесты для моделей и серверной логики.
  
2. Описание предметной области
   <img width="336" height="356" alt="image" src="https://github.com/user-attachments/assets/3ed7686a-c900-409e-adaf-994a9f34c5fb" />
   1. app.py : сущность приложения, параметры - имя автора и версия приложения
   2. author.py : сущность автора, параметры - имя и группа автора
   3. currency.py : сущность валюты, параметры - id валюты, цифровой код, символьный код, название, курс валюты и номинал
   4. user.py : сущность пользователя, параметры - id и имя пользователя
   5. userCurrency : подписка на валюту, хранит id некоторого пользователя и некоторой валюты

3. Структура проекта
   <img width="1390" height="1032" alt="image" src="https://github.com/user-attachments/assets/48e81de6-a444-4610-bd2a-63c97c4108c5" />
   1. models - модели, описаны выше
   2. templates - html-шаблоны, создают страницы index (главная), author (информация об авторе), courses (таблица с курсами валют), users (список пользователей сайта)
   3. utils/currencies_api.py - функция get_currencies, получающая актуальные курсы валют 
   4. controller_test.py - тесты контроллеров внутри myapp.py, models_test - тесты моделей, get_cur_test - тест функции get_currencies.
   5. myapp.py - главный файл, запускающий сервер. Внутри него рендерятся страницы.

4. Описание реализации
   1. геттеры получают значения, сеттеры устанавливают значения и проверяют их на корректность. Например, author.group должно меть не менее 5 символов в строке.
   2. после запуска сервера пользователь попадает на страницу index ('/'). при переходе на следующие страницы формируется соответствующий маршрут ('/users' для страницы, соответсвующей шаблону users.html)
   3. <img width="900" height="204" alt="image" src="https://github.com/user-attachments/assets/842288f9-da95-4522-83a7-bccfd1d89e61" />
      Страницы создаются с помощью Jinja2. C помощью FileSystemLoader Jinja2 использует в качестве html-шаблонов папку templates. При активации маршрутов происходит рендеринг соответствующих маршруту html-файлов (это происходит в myapp.py)
   4. get_currencies находится в utils/currencies_api.py и используется для получения словаря, при рендеринге передающегося в courses.html
      <img width="1138" height="582" alt="image" src="https://github.com/user-attachments/assets/11568ed9-a9f3-4a2e-b4de-3a5228a82a5b" />

5. Примеры работы приложения:
   <img width="3024" height="1964" alt="image" src="https://github.com/user-attachments/assets/38044372-e172-4487-89d7-1ea051d47c4e" />
   <img width="3024" height="1964" alt="image" src="https://github.com/user-attachments/assets/5da3531d-eaae-460a-9d3c-00d09db22eb9" />
   <img width="3024" height="1964" alt="image" src="https://github.com/user-attachments/assets/ded25bef-dc60-4ee4-a77e-cdbaa89bcebf" />
   <img width="3024" height="1964" alt="image" src="https://github.com/user-attachments/assets/8a90644c-3599-4239-8a29-c7c0f0c65bc9" />


6. Тестирование:
   get _cur_test.py
   <img width="1390" height="1508" alt="image" src="https://github.com/user-attachments/assets/a1092c26-003e-4f1d-b408-259617a139d2" />
   Вывод: Ran 4 tests in 0.001s
OK

   models_test.py
   <img width="1390" height="1224" alt="image" src="https://github.com/user-attachments/assets/b4780c58-dd2e-400d-8591-274fc677ef5e" />
   Вывод: Ran 3 tests in 0.000s
OK

   contoller_test.py
   <img width="1390" height="1508" alt="image" src="https://github.com/user-attachments/assets/994c8b97-a6eb-4f9c-8bb9-56be8a7d1b79" />
   Вывод: Ran 4 tests in 0.038s
OK

7. Выводы
   В ходе выполнения лабораторной работы было успешно реализовано клиент-серверное приложение на чистом Python без использования сторонних веб-фреймворков. Я изучила и применила основы веб-разработки: обработка HTTP-запросов через http.server, маршрутизация, работа с шаблонами и управление данными. Была применена архитектура MVC: model, view, controller. Кроме того, был разработан полный набор автоматизированных тестов. Все тесты проходят успешно, что подтверждает корректность реализации и устойчивость приложения к некорректным входным данным.

   


 
   

