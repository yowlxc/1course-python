"""Модуль с классом пользователя."""


# id — уникальный идентификатор
# name — имя пользователя


class User:
    """Представляет пользователя с уникальным ID и именем."""
    _next_id = 1

    def __init__(self, name: str) -> None:
        """Инициализирует пользователя.

        Args:
            name: Имя пользователя.
        """
        if not isinstance(name, str) or len(name) < 2:
            raise ValueError('Ошибка при задании имени пользователя')
        self.__id = User._next_id
        User._next_id += 1
        self.__name = name

    @property
    def id(self) -> int:
        """Возвращает уникальный идентификатор пользователя."""
        return self.__id

    @property
    def name(self) -> str:
        """Возвращает имя пользователя."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Устанавливает имя пользователя.

        Args:
            name: Имя пользователя.

        Raises:
            ValueError: Если имя не строка или короче 2 символов.
        """
        if type(name) is str and len(name) >= 2:
            self.__name = name
        else:
            raise ValueError('Ошибка при задании имени пользователя')