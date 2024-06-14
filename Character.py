from Classes import Character


class Character(Character):
    def __doc__(self) -> str:
        return "Hello"

    def __init__(self, name: str | None = None, path: str | None = None) -> None:
        match name:
            case None: self.name = ""
            case _: self.name = name
        match path:
            case None: self.path = ""
            case _: self.path = path
        self.db = {
            "Имя": self.name,
            "Путь": self.path,
            "Основные": {
                "Обычная атака": 1,
                "Навык": 1,
                "Сверхспособность": 1, },
            "Первая ветка": [0, 0, 0],
            "Вторая ветка": [0, 0, 0],
            "Третья ветка": [0, 0, 0, 0],
        }
        return None

    def __del__(self) -> bool:
        return bool(self)

    def __str__(self) -> str:
        return f"{self.name}\t{self.path}\n{self.db}"

    def __bool__(self) -> bool:
        match len(self.name):
            case 0: return True
            case _: return False

    def __getitem__(self, mark: str) -> any:
        return self.db[mark]

    def __setitem__(self, mark: str, value: int | str, parametr: str | int | None = None) -> None:
        match parametr:
            case None:
                if mark == "Имя" or mark == "Путь":
                    self.db[mark] = value
                else:
                    print("error")
            case _:
                self.db[mark][parametr] = value
        return None

    def __delitem__(self, mark: str, parametr: str | int | None = None) -> None:
        match mark:
            case "Имя":
                self.db[mark] = ""
            case "Основные":
                self.db[mark][parametr] = 1
            case _:
                self.db[mark][parametr] = 0
        return None

    def Change(self, mark: str, value: int | str, parametr: str | int | None = None) -> None:
        self.__setitem__(mark, value, parametr)
        return None

    def Reset(self, mark: str, parametr: str | int | None = None) -> None:
        self.__delitem__(mark, parametr)


if __name__ == "__main__":
    a = Character()
    print(a)
    a.Change("Имя", "March 7")
    print(a)
    a.Change("Путь", "Сохранение")
    print(a)
