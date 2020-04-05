import json


class Person:

    def __init__(self, first_name, surname, age):
        self._first_name = first_name
        self._surname = surname
        self._age = age

    def meth(self):
        pass


class PersonEncoder(json.JSONEncoder):

    def default(self, person):
        if isinstance(person, Person):
            return person.__dict__
        else:
            return json.JSONEncoder.default(self, person)


person = {
    'first_name': 'Math',
    'surname': 'Daemon',
    'age': 30,
    'interests': ['football', 'math']
}

person_obj = Person('John', 'Doe', 40)


person = json.dumps(person)
print(person)


person_serialized = json.dumps(person_obj, cls=PersonEncoder, indent=4)
print(person_serialized)

person_deserialized = json.loads(person_serialized)
print(person_deserialized)
print(type(person_deserialized))
