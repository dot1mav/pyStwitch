__all__ = ['SwitchFunc', 'SwitchBool']

from typing import Any


class SwitchFunc:
    def set_func(self, key: Any):

        def wrapper(func):
            self.__dict__.update({key: func})

        return wrapper

    def set_conditions(self, conditions: dict) -> None:
        for key in conditions:
            self.__dict__.update({key: conditions[key]})

    def set_condition(self, key: Any, func) -> None:
        self.__dict__.update({key: func})

    def get_conditions(self) -> dict:
        return self.__dict__

    def get_condition(self, key) -> Any:
        return self.__dict__[key] if key in self.__dict__.keys() else None

    def del_condition(self, key: Any) -> bool:
        if key in self.__dict__.keys():
            self.__dict__.pop(key)
            return True
        return False

    def del_conditions(self, conditions: dict) -> None:
        for key in conditions:
            if key in self.__dict__.keys():
                self.__dict__.pop(key)

    def check_attr(self, attr: Any) -> bool:
        for key in self.__dict__.keys():
            if attr == key:
                self.__dict__[key]()
                return True
        return False

    def __call__(self, attr: Any) -> bool:
        return self.check_attr(attr)

    def __repr__(self) -> str:
        return f'keys -> {[key for key in self.__dict__.keys()]}'

    def __str__(self) -> str:
        return str(self.__dict__)


class SwitchBool:
    def __init__(self) -> None:
        self.__list__ = list()

    def set_key(self, key: Any) -> None:
        self.__list__.append(key)

    def set_keys(self, keys: list) -> None:
        for key in keys:
            self.__list__.append(key)

    def del_key(self, key: Any) -> None:
        if key in self.__list__:
            self.__list__.remove(key)

    def del_keys(self, keys: list):
        for key in keys:
            if key in self.__list__:
                self.__list__.remove(key)

    def __call__(self, key) -> bool:
        return True if key in self.__list__ else False

    def __repr__(self) -> str:
        return f'keys -> {self.__list__}'

    def __str__(self) -> str:
        return str(self.__list__)
