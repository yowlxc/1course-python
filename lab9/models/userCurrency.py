"""Модуль с классом связи пользователя и валюты."""

from typing import NoReturn


class UserCurrency:
    """Представляет связь пользователя с валютой (подписку)."""

    def __init__(self, id_: int, user_id: int, currency_id: int) -> None:
        """Инициализирует связь пользователя и валюты.

        Args:
            id_: Уникальный идентификатор записи.
            user_id: Идентификатор пользователя.
            currency_id: Идентификатор валюты.
        """
        self.id = id_
        self.user_id = user_id
        self.currency_id = currency_id

    @property
    def id(self) -> int:
        """Возвращает уникальный идентификатор записи."""
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        """Устанавливает уникальный идентификатор записи.

        Args:
            value: Уникальный идентификатор.

        Raises:
            ValueError: Если значение не является целым положительным числом.
        """
        if isinstance(value, int) and value > 0:
            self.__id = value
        else:
            raise ValueError("Ошибка при задании уникального идентификатора")

    @property
    def user_id(self) -> int:
        """Возвращает идентификатор пользователя."""
        return self.__user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        """Устанавливает идентификатор пользователя.

        Args:
            value: Идентификатор пользователя.

        Raises:
            ValueError: Если значение не является целым положительным числом.
        """
        if isinstance(value, int) and value > 0:
            self.__user_id = value
        else:
            raise ValueError("Ошибка при задании ID пользователя")

    @property
    def currency_id(self) -> int:
        """Возвращает идентификатор валюты."""
        return self.__currency_id

    @currency_id.setter
    def currency_id(self, value: int) -> None:
        """Устанавливает идентификатор валюты.

        Args:
            value: Идентификатор валюты.

        Raises:
            ValueError: Если значение не является целым положительным числом.
        """
        if isinstance(value, int) and value > 0:
            self.__currency_id = value
        else:
            raise ValueError("Ошибка при задании идентификатора валюты")