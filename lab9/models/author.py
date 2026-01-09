"""Модуль с классом автора."""


# name — имя автора
# group — учебная группа


class Author:
    """Представляет автора с именем и учебной группой."""

    def __init__(self, name: str, group: str) -> None:
        """Инициализирует автора.

        Args:
            name: Имя автора.
            group: Учебная группа автора.
        """
        self.__name: str = name
        self.__group: str = group

    @property
    def name(self) -> str:
        """Возвращает имя автора."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Устанавливает имя автора.

        Args:
            name: Имя автора.

        Raises:
            ValueError: Если имя не является строкой или короче 2 символов.
        """
        if type(name) is str and len(name) >= 2:
            self.__name = name
        else:
            raise ValueError('Ошибка при задании имени автора')

    @property
    def group(self) -> str:
        """Возвращает учебную группу автора."""
        return self.__group

    @group.setter
    def group(self, group: str) -> None:
        """Устанавливает учебную группу автора.

        Args:
            group: Учебная группа автора.

        Raises:
            ValueError: Если группа не является строкой или не длиннее 5 символов.
        """
        if type(group) is str and len(group) > 5:
            self.__group = group
        else:
            raise ValueError('Ошибка при задании группы автора')