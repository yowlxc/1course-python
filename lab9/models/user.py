"""Модуль с классом пользователя."""

from typing import NoReturn


class User:
    """Представляет пользователя с уникальным ID и именем."""

    _next_id: int = 1

    def __init__(self, name: str) -> None:
        """Инициализирует пользователя.

        Args:
            name: Имя пользователя. Должно быть строкой длиной не менее 2 символов.

        Raises:
            ValueError: Если имя не является строкой или короче 2 символов.
        """
        self.name = name
        self.__id: int = User._next_id
        User._next_id += 1

    @property
    def id(self) -> int:
        """Возвращает уникальный идентификатор пользователя."""
        return self.__id

    @property
    def name(self) -> str:
        """Возвращает имя пользователя."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Устанавливает имя пользователя.

        Args:
            value: Имя пользователя.

        Raises:
            ValueError: Если значение не является строкой или короче 2 символов.
        """
        if isinstance(value, str) and len(value) >= 2:
            self.__name = value
        else:
            raise ValueError("Ошибка при задании имени пользователя")