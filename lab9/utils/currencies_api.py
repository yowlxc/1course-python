"""Модуль для получения курсов валют с API Центробанка РФ."""

from datetime import datetime
import requests


def get_currencies(currency_codes=None, url: str = "https://www.cbr-xml-daily.ru/daily_json.js"):
    """Получает курсы валют с API Центробанка России.

    Args:
        currency_codes (list, optional): Список символьных кодов валют
            (например, ['USD', 'EUR']). Если None — возвращаются все валюты
            из ответа.
        url (str): URL API для запроса курсов. По умолчанию — официальный
            эндпоинт ЦБ РФ.

    Returns:
        dict: Словарь, где ключи — символьные коды валют, а значения — их курсы.
        Возвращает словарь даже при частичном совпадении: если валюта не найдена,
        её значение будет строкой с сообщением об ошибке.

    Raises:
        ConnectionError: При ошибках сети или недоступности API.
        ValueError: При некорректном JSON-ответе.
        KeyError: Если в ответе отсутствует ключ 'Valute'.
        TypeError: Если значение курса имеет неверный тип.

    Examples:
        >>> rates = get_currencies(['USD', 'EUR'])
        >>> isinstance(rates['USD'], float)
        True
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError as e:
            raise ValueError("Некорректный JSON") from e

        if "Valute" not in data:
            raise KeyError("Ответ не содержит ключа 'Valute'")

        # Если currency_codes не задан — берём все доступные коды
        if currency_codes is None:
            currency_codes = list(data["Valute"].keys())

        currencies = {}
        for code in currency_codes:
            if code in data["Valute"]:
                value = data["Valute"][code]["Value"]
                if not isinstance(value, (int, float)):
                    raise TypeError(f"Курс валюты '{code}' имеет неверный тип")
                currencies[code] = value
            else:
                currencies[code] = f"Код валюты '{code}' не найден"

        return currencies

    except requests.exceptions.ConnectionError as e:
        raise ConnectionError("API недоступен") from e
    except requests.exceptions.Timeout as e:
        raise ConnectionError("Превышен лимит времени при подключении к API") from e
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Ошибка запроса к API: {e}") from e