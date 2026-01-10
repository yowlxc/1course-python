Отчёт по лабораторной работе №9
1. Цели работы:
    1. Реализовать CRUD (Create, Read, Update, Delete) для сущностей бизнес-логики приложения.
    2. Освоить работу с SQLite в памяти (:memory:) через модуль sqlite3.
    3. Понять принципы первичных и внешних ключей и их роль в связях между таблицами.
    4. Выделить контроллеры для работы с БД и для рендеринга страниц в отдельные модули.
    5. Использовать архитектуру MVC и соблюдать разделение ответственности.
    6. Отображать пользователям таблицу с валютами, на которые они подписаны.
    7. Реализовать полноценный роутер, который обрабатывает GET-запросы и выполняет сохранение/обновление данных и рендеринг страниц.
    8. Научиться тестировать функционал на примере сущностей currency и user с использованием unittest.mock.

2. Описание моделей, их свойств и связей.
   связь между моделями происходит через внешние ключи
       app.py : сущность приложения, параметры - название и версия приложения
       author.py - сущность автора, парамтетры - имя и номер группы автора
       currencies.py - сущность валюты, параметры - числовой код, символьный код, название, номинал, курс валюты и id валюты
       user.py - сущность пользователя, параметры - имя и id пользователя
       userCurrency.py - сущность подписки пользователя, параметры - собственный id, id некоторого пользователя и id некоторой валюты
   
3. Структура проекта с назначением файлов.
  <img width="2046" height="1138" alt="image" src="https://github.com/user-attachments/assets/1e7cd3bb-62fe-46c2-9bec-95505c64029b" />
   проект содержит 4 папки и 2 файла вне них
   1. папка models - модели, описаны в пункте 2.
   2. папка contollers - контроллеры
       1. databasecontroller.py - работа с базами данных (sqlite)
       2. pages.py - рендерит страницы сайта
          
   3. папка templates - html-шаблоны для страниц сайта
   4. utils/currencies_api.py - функция get_currencies, передаёт актуальные курсы валют с сайта центробанка
   5. myapp.py - главный файл, запускающий сервер
   6. test_user_and_currency.py - тестирование сущностей user и currency с помощью unittest.mock

4. Реализацию CRUD с примерами SQL-запросов.
   <img width="1380" height="976" alt="image" src="https://github.com/user-attachments/assets/89ad8117-a806-4214-a645-3919679346a6" />
   <img width="1498" height="570" alt="image" src="https://github.com/user-attachments/assets/0b04546e-6b4e-40dd-bac9-66581aa121b8" />

   C - Create: INSERT INTO...
   R - Read: def get_currency_by_id()
   U - Update: def update_currency_value()
   D - Delete: def delete_currency()
   
5. Скриншоты работы приложения (главная страница, таблица валют, обновление и удаление).
   <img width="3024" height="1964" alt="image" src="https://github.com/user-attachments/assets/2370c065-f68f-4c5d-affa-e29ec6844aae" />
    <img width="3024" height="1964" alt="image" src="https://github.com/user-attachments/assets/d123fec7-6e88-4a30-aadd-6f06ef87c64e" />
    <img width="1512" height="982" alt="Снимок экрана 2026-01-10 в 13 24 16" src="https://github.com/user-attachments/assets/5625de30-d98a-4c35-affd-80d7fe801b3e" />
    <img width="3024" height="1964" alt="image" src="https://github.com/user-attachments/assets/60471789-141f-4060-9899-3afc8542a863" />
    <img width="3024" height="1964" alt="image" src="https://github.com/user-attachments/assets/50ae889e-5a4d-46a9-9d8a-7a8e81823f63" />
    
6. Примеры тестов с unittest.mock и результаты их выполнения.

<img width="1498" height="872" alt="image" src="https://github.com/user-attachments/assets/bccb709c-4382-460c-8bb0-6d061cdfffde" />
<img width="1498" height="1152" alt="image" src="https://github.com/user-attachments/assets/445bb2ac-c4d5-474d-87b5-bcf8fec09951" />
<img width="1498" height="732" alt="image" src="https://github.com/user-attachments/assets/262dfb9a-1a12-4076-abba-e6601f741190" />
<img width="2254" height="222" alt="image" src="https://github.com/user-attachments/assets/96542bf8-69c0-42f6-b8d7-5ae7aa1c33a1" />
    
7. Выводы о применении MVC, работе с SQLite, обработке маршрутов и рендеринге шаблонов.
   Мной был создан проект на основе архитектуры MVC: Models (папка models) + view (папка templates) + controllers (папка controllers)
    

    
