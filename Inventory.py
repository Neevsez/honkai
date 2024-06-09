from Materials import Material

class Inventory:
    def __str__(self):
        for item in self.db:
            print(item, self.db[item])
        return "\n"
    
    def __bool__(self):
        for item in self.db:
            match bool(item):
                case 0 | False | None:
                    continue
                case 1 | True:
                    return True
        return False

    def __init__(self):
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

    def __del__(self): return bool(self)

    def __getitem__(self, Material_Type):
        return self.db[Material_Type]

    def Add(self, type, *values):
        a, b, c = values
        self.db[type] += a, b, c
        return self

    def Sub(self, type, *values):
        a, b, c = values
        self.db[type] -= a, b, c
        return self
