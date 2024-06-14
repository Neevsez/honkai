from Character import Character
from Inventory import Inventory
from Classes import Calculate
from Materials import Material


class Calculate(Calculate):
    def __get_line(self, num: bool = False) -> tuple[str]:
        q = input(": ")
        match num:
            case 0 | False | None:
                f = q.replace(", ", ",")
                q = f.split(",")
            case 1 | True:
                f = q.replace(" ", ",")
                q = f.split(",")
        f = []
        for i in range(len(q)):
            if q[i] == "":
                continue
            else:
                f.append(q[i])
        del q
        return tuple(f)
    
    def __check_path(self) -> str:
        match self.character.path:
            case "": return None
            case "Сохранение_1": return "Щиты"
            case "Сохранение_2": return "Янтарь"
            case "Разрушение_1": return "Мечи"
            case "Разрушение_2": return "Клыки"
            case "Охота_1": return "Стрелы"
            case "Охота_2": return "Пули"
            case "Гармония_1": return "Шкатулки"
            case "Гармония_2": return "Ноты"
            case "Эрудиция_1": return "Ключи"
            # case "Эрудиция_2": return
            case "Небытие_1": return "Обсидиан"
            case "Небытие_2": return "Духи"
            case "Изобилие_1": return "Цветы"
            case "Изобилие_2": return "Фрукты"

    def __doc__(self) -> str:
        return "Hello"

    def __init__(self, type:str = "4*", character: Character | None = None, inventory: Inventory | None = None) -> None:
        match character:
            case None: self.character = Character("4*")
            case _: self.character = character
        match inventory:
            case None: self.inventory = Inventory()
            case _: self.inventory = inventory

    def __str__(self):
        return f"{self.inventory.__str__()}{self.character.__str__()}"

    def UpdateInventory(self) -> None:
        n = self.__get_line()
        for i in range(len(n)):
            q = self.__get_line(True)
            if n[i] == "Кредиты":
                self.inventory.Update(n[i], q[0])
            else:
                self.inventory.Update(n[i], mat=Material(args=q))
        return None

    def ChangeCharacter(self, keyboard = True, **kwargs) -> None:
        match keyboard:
            case True | 1:
                n = self.__get_line()
                for i in range(len(n)):
                    q = self.__get_line()
                    if n[i] == "Имя" or n[i] == "Путь":
                        self.character.Change(n[i], q[0])
                    else:
                        self.character.Change(n[i], int(q[0]), q[1])
            case False | 0 | None:
                for item in kwargs:
                    if item == "Имя" or item == "Путь":
                        self.character.Change(item, kwargs[item])
                    else:
                        self.character.Change(item, kwargs[item][0], kwargs[item][1])
        return None
    
    def UpdateCharacter(self, mark:str) -> None:
        q = self.__check_path()


a = Calculate()
b = a.inventory
c = a.character
a.ChangeCharacter(False, Имя="Март 7", Путь="Сохранение_1")
