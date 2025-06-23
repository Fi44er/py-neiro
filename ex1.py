class Point:
    color = "red"
    circle = 2

    MIN_COORD = -10
    MAX_COORD = 10

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __new__(cls, *args, **kwargs):  # ссылается на текущий класс
        print("void __new__ for " + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):  # ссылается на экземпляр
        if self.validate(x) and self.validate(y):
            print("init")
            self.x = x
            self.y = y

    def __del__(self):
        print("Deleting1: " + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y


class DB:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, path):
        self.path = path

    def __del__(self):
        DB.__instance = None
        print("Deleting: " + str(self))

    def connect(self):
        print("Connect to " + self.path)

    def close(self):
        print("Close connection to " + self.path)


# pt = Point(0, 4)
# print(pt)

print(Point.validate(50))

db = DB("test.db")
db.connect()
db.close()
