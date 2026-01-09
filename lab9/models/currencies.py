"""Модуль с классом валюты."""


# id — уникальный идентификатор
# num_code — цифровой код
# char_code — символьный код
# name — название валюты
# value — курс
# nominal — номинал (за сколько единиц валюты указан курс)


class Currency:
    _next_id = 1
    """Представляет валюту с кодами, названием, курсом и номиналом."""

    def __init__(
        self,
        num_code: str,
        char_code: str,
        name: str,
        value: float,
        nominal: int
    ) -> None:
        """Инициализирует валюту.

        Args:
            id: Уникальный идентификатор валюты.
            num_code: Цифровой код валюты.
            char_code: Символьный код валюты (3 буквы).
            name: Название валюты.
            value: Курс валюты.
            nominal: Номинал (за сколько единиц валюты указан курс).
        """
        self.__id = Currency._next_id
        Currency._next_id += 1
        self.num_code = num_code
        self.char_code = char_code
        self.name = name
        self.value = value
        self.nominal = nominal

    @property
    def id(self) -> int:
        """Возвращает уникальный идентификатор валюты."""
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        """Устанавливает уникальный идентификатор валюты.

        Args:
            id: Уникальный идентификатор.

        Raises:
            ValueError: Если ID не является целым числом или не больше 0.
        """
        if isinstance(id, int) and id > 0:
            self.__id = id
        else:
            raise ValueError('Ошибка при задании ID')

    @property
    def num_code(self) -> int:
        """Возвращает цифровой код валюты."""
        return self.__num_code

    @num_code.setter
    def num_code(self, num_code: int) -> None:
        """Устанавливает цифровой код валюты.

        Args:
            num_code: Цифровой код.

        Raises:
            ValueError: Если код не является целым числом.
        """
        if isinstance(num_code, int):
            self.__num_code = num_code
        else:
            raise ValueError('Ошибка при задании цифрового кода')

    @property
    def char_code(self) -> str:
        """Возвращает символьный код валюты."""
        return self.__char_code

    @char_code.setter
    def char_code(self, char_code: str) -> None:
        """Устанавливает символьный код валюты.

        Args:
            char_code: Символьный код (должен быть длиной 3 символа).

        Raises:
            ValueError: Если код не строка или не длиной 3 символа.
        """
        if isinstance(char_code, str) and len(char_code) == 3:
            self.__char_code = char_code.upper()
        else:
            raise ValueError('Ошибка при задании символьного кода')

    @property
    def name(self) -> str:
        """Возвращает название валюты."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Устанавливает название валюты.

        Args:
            name: Название валюты.

        Raises:
            ValueError: Если название не строка или короче 2 символов.
        """
        if isinstance(name, str) and len(name) >= 2:
            self.__name = name
        else:
            raise ValueError('Ошибка при задании названия валюты')

    @property
    def value(self) -> float:
        """Возвращает курс валюты."""
        return self.__value

    @value.setter
    def value(self, value: float) -> None:
        """Устанавливает курс валюты.

        Args:
            value: Курс валюты.

        Raises:
            ValueError: Если значение не является числом с плавающей точкой или неположительно.
        """
        if isinstance(value, (int, float)) and value > 0:
            self.__value = float(value)
        else :
            raise ValueError('Ошибка при задании курса')

    @property
    def nominal(self) -> float:
        """Возвращает номинал валюты."""
        return self.__nominal

    @nominal.setter
    def nominal(self, nominal: float) -> None:
        """Устанавливает номинал валюты.

        Args:
            nominal: Номинал валюты.

        Raises:
            ValueError: Если значение не является числом с плавающей точкой.
        """
        if isinstance(nominal, float):
            self.__nominal = nominal
        else:
            raise ValueError('Ошибка при задании номинала')