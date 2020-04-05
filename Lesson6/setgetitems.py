class MyStruct:

    def __init__(self, *args):
        self.container = [*args]

    def __getitem__(self, item):
        return self.container[item]

    def __setitem__(self, key, value):
        self.container[key] = value

    def setvalueto1(self):
        self[1] = 100


a = MyStruct(1, 2, 3, 4, 5)
