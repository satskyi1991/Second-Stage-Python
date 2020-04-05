def method(obj):
    print('Hi')

MyCl = type(
    'MyClass',
    (),
    {
        'the_first_attr': 1,
        'get_smth': method
    }

)

obj_of_my_cl = MyCl()
print(obj_of_my_cl.get_smth())



class UsefullMethods:

    def make_class_feel_good(self):
        print('Feeling good')


class MyMeta(type):

    def __new__(mcls, name, bases, attributes):
        bases += (UsefullMethods, object)
        print(mcls, name, bases, attributes)
        return super().__new__(mcls, name, bases, attributes)


class Point_1(metaclass=MyMeta):

    name = 'PointClass'

    def __init__(self, x):
        self.x = x

print(Point_1.__bases__)

"""
Метакласс занимается созданием других классов.
Все классы в python созданы type().
Метаклассы нужны для управления созданием классов, изменения имени, 
базовых классов, и атрибутов.
"""
