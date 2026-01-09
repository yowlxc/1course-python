"""Модуль с классом связи пользователя и валюты."""


# id — уникальный идентификатор
# user_id — внешний ключ к User
# currency_id — внешний ключ к Currency


class UserCurrency:
    """Представляет связь пользователя с валютой."""

    def __init__(self, id: int, user_id: int, currency_id: int) -> None:
        """Инициализирует связь пользователя и валюты.

        Args:
            id: Уникальный идентификатор записи.
            user_id: ID пользователя.
            currency_id: ID валюты.
        """
        self.__id: int = id
        self.__user_id: int = user_id
        self.__currency_id: int = currency_id

    @property
    def id(self) -> int:
        """Возвращает уникальный идентификатор записи."""
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        """Устанавливает уникальный идентификатор записи.

        Args:
            id: Уникальный идентификатор.

        Raises:
            ValueError: Если ID не целое число или не больше 0.
        """
        if type(id) is int and id > 0:
            self.__id = id
        else:
            raise ValueError('Ошибка при задании уникального идентификатора')

    @property
    def user_id(self) -> int:
        """Возвращает ID пользователя."""
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: int) -> None:
        """Устанавливает ID пользователя.

        Args:
            user_id: ID пользователя.

        Raises:
            ValueError: Если ID не целое число или не больше 0.
        """
        if type(user_id) is int and user_id > 0:
            self.__user_id = user_id
        else:
            raise ValueError('Ошибка при задании ID пользователя')

    @property
    def currency_id(self) -> int:
        """Возвращает ID валюты."""
        return self.__currency_id

    @currency_id.setter
    def currency_id(self, currency_id: int) -> None:
        """Устанавливает ID валюты.

        Args:
            currency_id: ID валюты.

        Raises:
            ValueError: Если ID не целое число или не больше 0.
        """
        if type(currency_id) is int and currency_id > 0:
            self.__currency_id = currency_id
        else:
            raise ValueError('Ошибка при задании идентификатора валюты')