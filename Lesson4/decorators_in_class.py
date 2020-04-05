"""
Для использования декораторов с методами, декораторы следует объявлять:
1) Вне класса
2) В другом классе помечая декоратором @staticmethod
3) Внутри текущего класса еще одним классом
"""
class A:

    class Decorators:

        @staticmethod
        def dec(func):
            def wrapper(*args):
                func(*args)

            return wrapper

    @Decorators.dec
    def do_smth(self, arg1, arg2):
        pass




a = A()
a.do_smth(1, 2)
