from Materials import Material
from Classes import Inventory


class Inventory(Inventory):
    def __doc__(self) -> str:
        return "Hello"

    def __init__(self) -> None:
        self.db = {
            "Кредиты": 0,
            # for heroes path
            "Книги опыта": Material(0, 0, 0),
            "Эфир": Material(0, 0, 0),
            "Мечи": Material(0, 0, 0),
            "Стрелы": Material(0, 0, 0),
            "Ключи": Material(0, 0, 0),
            "Щиты": Material(0, 0, 0),
            "Обсидиан": Material(0, 0, 0),
            "Шкатулки": Material(0, 0, 0),
            "Цветы": Material(0, 0, 0),
            "Клыки": Material(0, 0, 0),
            "Пули": Material(0, 0, 0),
            "Янтарь": Material(0, 0, 0),
            "Духи": Material(0, 0, 0),
            "Ноты": Material(0, 0, 0),
            "Фрукты": Material(0, 0, 0),
            # other
            "Ядра": Material(0, 0, 0),
            "Антиматерия": Material(0, 0, 0),
            "Знаки отличия": Material(0, 0, 0),
            "Древние детали": Material(0, 0, 0),
            "Ветви дерева": Material(0, 0, 0),
            "Механические запчасти": Material(0, 0, 0),
            "Сны": Material(0, 0, 0),
            "Воспоминания": Material(0, 0, 0),
            # from week bosses
            "Дракон": Material(0, 0, 0),
            "Коколия": Material(0, 0, 0),
            "Фантилия": Material(0, 0, 0),
            "Жук": Material(0, 0, 0),
            # from shadows
            "Гвоздь обезьяны": Material(0, 0, 0),
            "Эндотермический хитин": Material(0, 0, 0),
            "Восходящий мусор": Material(0, 0, 0),
            "Молниеносный посох Оборотня": Material(0, 0, 0),
            "Разрешение IPC на работу": Material(0, 0, 0),
            "Молниеносная корона Тени прошлого": Material(0, 0, 0),
            "Штормовой глаз": Material(0, 0, 0),
            "Студенистый хитин": Material(0, 0, 0),
            "Бешеное сердце": Material(0, 0, 0),
            "Золотая корона тени прошлого": Material(0, 0, 0),
            "Холодильник мечты": Material(0, 0, 0),
            "Знак Преисподней": Material(0, 0, 0),
            "Запретительный указ": Material(0, 0, 0),
            "Пустое чугунное": Material(0, 0, 0),
            "Снежный рог": Material(0, 0, 0),
            "Огнемет мечты": Material(0, 0, 0),
            "Лезвие из обжигающей стали": Material(0, 0, 0),
            "Сломанные зубы Железного Волка": Material(0, 0, 0),
        }

    def __del__(self) -> bool: return bool(self)

    def __str__(self) -> str:
        for item in self.db:
            print(item, self.db[item], sep="\n")
        return "\t"

    def __bool__(self) -> bool:
        for item in self.db:
            match bool(item):
                case 0 | False | None:
                    continue
                case 1 | True:
                    return True
        return False

    def __getitem__(self, Material_Type) -> any:
        return self.db[Material_Type]

    def __setitem__(self, Material_Type: str, index: int, value: int) -> None:
        self.db[Material_Type][index] = value
        return None

    def __delitem__(self, Material_Type: str) -> Material:
        q = self.db[Material_Type]
        del self.db[Material_Type]
        return q

    def Update(self, mark: str, value: int | None = None, parametr: str | None = None, mat:Material = None) -> None:
        match mat:
            case None:
                match parametr:
                    case None:
                        if mark == "Кредиты":
                            self.db[mark] = value
                        else:
                            print("error")
                    case "purple":
                        self.db[mark].x = value
                    case "blue":
                        self.db[mark].y = value
                    case "green":
                        self.db[mark].z = value
            case _:
                self.db[mark] = mat
        return None

    def Reset(self, mark: str, parametr: str | None = None) -> None:
        match parametr:
            case None:
                if mark == "Кредиты":
                    self.db[mark] = 0
                else:
                    print("error")
            case "purple":
                self.db[mark].x = 0
            case "blue":
                self.db[mark].y = 0
            case "green":
                self.db[mark].z = 0
        return None
