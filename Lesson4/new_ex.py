class Person:
    fields = ('id_', 'name', 'nickname')
    _instances = None

    def __new__(cls, *args, **kwargs):
        if cls._instances:
            return cls._instances
        else:
            cls._instances = super().__new__(cls)

            for field in cls.fields:

                setattr(cls._instances, field, 100)
            return cls._instances





a = Person()
print(a.id_, a.name, a.nickname )

"""
__new__ - Создает объект
__init__ - инициализирует уже созданный объект
сразу вызывается __new__ и далее __init__
"""

"""
p = Point
first calling __new__ then calling __init__
if new returns another type instance (not Point)
__init__ won`t be called
"""
