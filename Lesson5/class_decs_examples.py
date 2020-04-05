class FacebookAuth:

    api_url = 'facebook.com/'

    def __init__(self, login, password):
        self._login = login
        self._password = password

    def __call__(self, *args, **kwargs):
        print('Object has been called')

    @classmethod
    def validate(cls, login, password):
        print(login, password)


fb = FacebookAuth('zxc', 'vbn')

fb()

FacebookAuth.validate('ddasdsa', 'dasdasdas')


class Dec:

    def __init__(self, func):
        self.f = func

    def __call__(self, *args, **kwargs):
        print(args)
        print(f'Wrapping function {self.f.__name__}')
        self.f()

@Dec
def test():
    print('hello')

test(123, 232)
