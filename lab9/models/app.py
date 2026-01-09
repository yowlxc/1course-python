# name — название приложения
# version — версия приложения
# author — объект Author
from .author import Author


class App:
    """Представляет приложение с названием, версией и автором."""

    def __init__(self, name: str, version: str, author: Author) -> None:
        """Инициализирует приложение.

        Args:
            name: Название приложения.
            version: Версия приложения.
            author: Автор приложения.
        """
        self.__name: str = name
        self.__version: str = version
        self.__author: Author = author

    @property
    def name(self) -> str:
        """Возвращает название приложения."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Устанавливает название приложения.

        Args:
            name: Название приложения.

        Raises:
            ValueError: Если название не является строкой или короче 2 символов.
        """
        if type(name) is str and len(name) >= 2:
            self.__name = name
        else:
            raise ValueError('Ошибка при задании имени приложения')

    @property
    def version(self) -> str:
        """Возвращает версию приложения."""
        return self.__version

    @version.setter
    def version(self, version: str) -> None:
        """Устанавливает версию приложения.

        Args:
            version: Версия приложения.

        Raises:
            ValueError: Если версия не является строкой, короче 3 символов
                или не содержит точки.
        """
        if type(version) is str and len(version) >= 3 and '.' in version:
            self.__version = version
        else:
            raise ValueError('Ошибка при задании версии приложения')

    @property
    def author(self) -> Author:
        """Возвращает автора приложения."""
        return self.__author

    @author.setter
    def author(self, author: Author) -> None:
        """Устанавливает автора приложения.

        Args:
            author: Автор приложения.

        Raises:
            ValueError: Если передан не объект Author.
        """
        if type(author) is Author:
            self.__author = author
        else:
            raise ValueError('Ошибка при задании автора приложения')