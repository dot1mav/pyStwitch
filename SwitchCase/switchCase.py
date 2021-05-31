from typing import Any


class SwitchCase:
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
