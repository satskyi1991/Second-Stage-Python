from marshmallow import (
    Schema,
    fields,
    ValidationError,
    validates,
    validate
)

"""
Схемы используются для валидации и сериализации данных.
Названия аттрибутов схемы должны совпадать с названиями
сериализуемой/валидируемой модели
"""
class BusSchema(Schema):
    id = fields.String(dump_only=True)
    model_ = fields.String()
    seats = fields.Int(validate=validate.Range(min=4, max=100))

    #Валидатор внутри класса, использует специальный декоратор
    #Если хотим юзать вне класса, передаем функцию валидатор по аргументу
    #validate аттрибута
    @validates('model_')
    def validate_model(self, value):
        if value == 'Sprinter':
            raise ValidationError('Value cannot be Sprinter')

#Dump_only - указывает что аттрибут доступен только для чтения
#load_only - только для записи
class TripSchema(Schema):
    id = fields.String(dump_only=True)
    destination = fields.String()
    bus = fields.Nested(
        BusSchema,
        dump_only=True
    )


class TripPostSchema(TripSchema):
    bus = fields.String(load_only=True)

"""
Исходная схема TripSchema не подходит для записи, по этому мы 
переопределяем аттрибут bus в дочерней схеме TripPostSchema и делаем его loadable
"""

class PassengerSchema(Schema):

    name = fields.String(required=True)
    surname = fields.String(required=True)
    trip = fields.String(dump_only=True)
