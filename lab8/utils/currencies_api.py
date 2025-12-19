from datetime import datetime
import requests

def get_currencies(currency_codes=None, url: str = "https://www.cbr-xml-daily.ru/daily_json.js"):
    """
    Получает курсы валют с API Центробанка России.

    Args:
        currency_codes (list, optional): Список символьных кодов валют (например, ['USD', 'EUR']).
                                         Если None — возвращаются все валюты из ответа.

    Returns:
        dict: Словарь, где ключи - символьные коды валют, а значения - их курсы.
              Возвращает None в случае ошибки запроса.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            raise ValueError("Некорректный JSON")

        currencies = {}

        if "Valute" not in data:
            raise KeyError("Нет ключа Valute")

        # Если currency_codes не задан — берём все коды из ответа
        if currency_codes is None:
            currency_codes = list(data["Valute"].keys())

        for code in currency_codes:
            if code in data["Valute"]:
                value = data["Valute"][code]["Value"]
                if not isinstance(value, (int, float)):
                    raise TypeError(f"Курс валюты '{code}' имеет неверный тип")
                currencies[code] = value
            else:
                currencies[code] = f"Код валюты '{code}' не найден"

        return currencies

    except requests.exceptions.ConnectionError:
        raise ConnectionError("API недоступен")
    except requests.exceptions.Timeout:
        raise ConnectionError("Превышен лимит времени при подключении к API")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Ошибка запроса к API: {str(e)}")