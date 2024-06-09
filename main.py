from Materials import Material
from Inventory import Inventory
from Classes import __Character



def Main():
    a = Inventory()
    b = a["Книги опыта"]
    print(b)


if __name__ == "__main__":
    Main()
