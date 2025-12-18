# id — уникальный идентификатор
# num_code — цифровой код
# char_code — символьный код
# name — название валюты
# value — курс
# nominal — номинал (за сколько единиц валюты указан курс)

class Currency:
    def __init__(self, id: int, num_code: int, char_code: str, name: str, value: float, nominal: float):
        self.__id = id
        self.__num_code = num_code
        self.__char_code = char_code
        self.__name = name
        self.__value = value
        self.__nominal = nominal

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        if isinstance(id, int) and id > 0:
            self.__id = id
        else:
            raise ValueError('Ошибка при задании ID')

    @property
    def num_code(self):
        return self.__num_code

    @num_code.setter
    def num_code(self, num_code: int):
        if isinstance(num_code, int):
            self.__num_code = num_code
        else:
            raise ValueError('Ошибка при задании цифрового кода')

    @property
    def char_code(self):
        return self.__char_code

    @char_code.setter
    def char_code(self, char_code: str):
        if isinstance(char_code, str) and len(char_code) == 3:
            self.__char_code = char_code.upper()
        else:
            raise ValueError('Ошибка при задании символьного кода')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str) and len(name) >= 2:
            self.__name = name
        else:
            raise ValueError('Ошибка при задании названия валюты')

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        if isinstance(value, float):
            self.__value = float(value)
        else:
            raise ValueError('Ошибка при задании курса')

    @property
    def nominal(self):
        return self.__nominal

    @nominal.setter
    def nominal(self, nominal: float):
        if isinstance(nominal, float):
            self.__nominal = nominal
        else:
            raise ValueError('Ошибка при задании номинала')

