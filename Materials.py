from Classes import Material


class Material(Material):
    def __doc__(self):
        return "hello world"

    def __get_data(self, args):
        a = 0
        b = 0
        c = 0
        o = ...
        match len(args):
            case 0:
                return self.z
            case 1:
                a = args[0]
            case 2:
                a, b = args[0], args[1]
            case 3:
                a, b, c = args[0], args[1], args[2]
            case _:
                a, b, c, o = args[0], args[1], args[2], args[2:]
        return a, b, c, o

# constructor
    def __init__(self, purple: int = 0, blue: int = 0, green: int = 0, args: tuple = None):
        if args != None:
            a, b, c, _ = self.__get_data(args)
            self.x = a
            self.y = b
            self.z = c
        else:
            self.x = purple
            self.y = blue
            self.z = green

    def __del__(self): bool(self)

# data type
    def __str__(self):
        return f"purple: {self.x}\nblue: {self.y}\ngreen: {self.z}"

    def __bool__(self):
        if (self.x + self.y + self.z == 0):
            return False
        else:
            return True

    def __int__(self): return len(self)

    def __float__(self): return float(len(self))

    def __to_tuple__(self): return (self.x, self.y, self.z,)

    def __to_list__(self): return [self.x, self.y, self.z]

    def __to_dict__(self): return {
        "purple": self.x, "blue": self.y, "green": self.z}

    def __len__(self): return self.x * 9 + self.y * 3 + self.z

# index
    def __getitem__(self, index):
        if index in range(0, 3):
            match index:
                case 0:
                    return self.x
                case 1:
                    return self.y
                case 2:
                    return self.z
        else:
            return "Index out of range"

    def __setitem__(self, index: int, value: int):
        match index:
            case 0: self.x = value
            case 1: self.y = value
            case 2: self.z = value
            case _: return "Index out of range"
        return self

    def __delitem__(self, index: int):
        match index:
            case 0: self.x = 0
            case 1: self.y = 0
            case 2: self.z = 0
            case _: return "Index out of range"
        return self

# math operators
    def __add__(self, args: tuple):
        a, b, c, _ = self.__get_data(args)
        a += self.x
        b += self.y
        c += self.z
        return Material(a, b, c)

    def __sub__(self, args: tuple):
        a, b, c, _ = self.__get_data(args)
        a -= self.x
        b -= self.y
        c -= self.z
        return Material(a, b, c)

    def __iadd__(self, args: tuple):
        a, b, c, _ = self.__get_data(args)
        self.x += a
        self.y += b
        self.z += c
        return self

    def __isub__(self, args: tuple):
        a, b, c, _ = self.__get_data(args)
        self.x -= a
        self.y -= b
        self.z -= c
        return self

# logical operations
    def __lt__(self, args: tuple):
        a, b, c, _ = self.__get_data(args)
        return (self.x < a), (self.y < b), (self.z < c)

    def __le__(self, args: tuple):
        a, b, c, _ = self.__get_data(args)
        return (self.x <= a), (self.y <= b), (self.z <= c)

    def __gt__(self, args: tuple):
        a, b, c, _ = self.__get_data(args)
        return (self.x > a), (self.y > b), (self.z > c)

    def __ge__(self, args: tuple):
        a, b, c, _ = self.__get_data(args)
        return (self.x >= a), (self.y >= b), (self.z >= c)

    def __eq__(self, args: tuple):
        a, b, c, _ = self.__get_data(args)
        return (self.x == a), (self.y == b), (self.z == c)

    def __ne__(self, args: tuple):
        a, b, c, _ = self.__get_data(args)
        return (self.x != a), (self.y != b), (self.z != c)


def Main():
    a = Material(0, 0, 0)
    print(a)


if __name__ == "__main__":
    Main()
