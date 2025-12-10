import logging
from my_logger import logger
from get_currencies import get_currencies
import sys


# #Логирование в stdout
# @logger(handle=sys.stdout)
# def get_currencies_stdout(currency_codes):
#     return get_currencies(currency_codes)


# print("Логирование в stdout")
# try:
#     get_currencies_stdout(['USD', 'EUR'])
# except Exception as e:
#     print(f"Обработано исключение: {e}")

# 2. Файловое логирование
file_logger = logging.getLogger("currency_file")
file_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("log2.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
file_logger.addHandler(file_handler)


@logger(handle=file_logger)
def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0.
    Демонстрирует разные уровни логирования.
    """
    # Проверка типов
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        file_logger.error(f"ERROR: Некорректные типы данных: a={a}, b={b}, c={c}")
        raise TypeError("Коэффициенты должны быть числами")

    # Критическая ошибка: a=b=0
    if a == 0 and b == 0:
        file_logger.critical("CRITICAL: Оба коэффициента a и b равны 0. Уравнение не имеет смысла.")
        raise ValueError("a и b равны 0")

    discriminant = b ** 2 - 4 * a * c

    # Предупреждение: дискриминант < 0
    if discriminant < 0:
        file_logger.warning(f"WARNING: Дискриминант отрицательный (D={discriminant}). Корней нет.")
        return []

    # Расчет корней
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    file_logger.info(f"INFO: Два корня: x1={x1}, x2={x2}")
    return [x1, x2]
