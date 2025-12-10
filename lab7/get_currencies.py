import functools
import io
from datetime import datetime
import requests
import sys
import logging
from my_logger import logger

# logging.basicConfig(
#     filename='log1.log',      # ← имя файла
#     filemode='a',               # 'a' = добавлять, 'w' = перезаписывать
#     level=logging.INFO,         # минимальный уровень логов
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     encoding='utf-8'            # чтобы кириллица работалаsls -lls
# )
# log = logging.getLogger("l1")
# log.setLevel(logging.INFO)

# @logger(handle = log)
# @logger()
def get_currencies(currency_codes: list, url:str = "https://www.cbr-xml-daily.ru/daily_json.js")->dict:
    """
    Получает курсы валют с API Центробанка России.

    Args:
        currency_codes (list): Список символьных кодов валют (например, ['USD', 'EUR']).

    Returns:
        dict: Словарь, где ключи - символьные коды валют, а значения - их курсы.
              Возвращает None в случае ошибки запроса.
    """
    try:

        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP

        try:
            data = response.json()
        
        except requests.exceptions.JSONDecodeError:
            raise ValueError("Некорректный JSON")
 
        currencies = {}

        if "Valute" in data:
            for code in currency_codes:
                if code in data["Valute"]:
                    if not isinstance(data["Valute"][code]["Value"], (int, float)):
                        raise TypeError(f"Курс валюты '{code}' имеет неверный тип")
                    currencies[code] = data["Valute"][code]["Value"]
                else:
                    currencies[code] = f"Код валюты '{code}' не найден"
        else :
            raise KeyError(f"Нет ключа Valute")
        return currencies
    
    except requests.exceptions.ConnectionError:
        raise ConnectionError("API недоступен")
    
    except requests.exceptions.Timeout:
        raise ConnectionError("Превышен лимит времени при подключении к API")
    
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Ошибка запроса к API: {str(e)}")
    
