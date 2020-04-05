import mongoengine as ME
ME.connect('TestUsers', host='127.0.0.1', port=27017)


class UserLikes(ME.Document):

    name = ME.StringField(min_length=2, max_length=255)
    quantity = ME.IntField(min_value=0)

    def __str__(self):
        return self.name


class User(ME.Document):

    name = ME.StringField(min_length=2, max_length=255)
    login = ME.StringField(max_length=255, min_length=3, unique=True)
    password = ME.StringField(min_length=10, max_length=1024)
    interests = ME.ListField(ME.StringField())
    likes = ME.ReferenceField(UserLikes)

    def __str__(self):
        return f'{self.id}_{self.name}'


if __name__ == '__main__':
    pass
