def func_a(a):
    def func_b(b):
        def func_c(c):
            def func_d(d):
                print(a, b, c, d)
            return func_d
        return func_c
    return func_b


result = func_a(10)(20)(30)(40)


def decorator(write_to_file):
    def actual_decorator(func_to_decorate):

        def wrapper(*args):
            result = func_to_decorate(*args)

            if write_to_file:
                file = open('logs.txt', 'w')
                file.write(result)
                file.close()
            else:
                print(result)
            return result, 12

        return wrapper
    return actual_decorator


@decorator(write_to_file=True)
def func_test(string_to_test, second_string_to_test):
    return string_to_test + second_string_to_test

#Source
# decorator(True)(func_test)('ZXC', 'QWE')
# print(r)

func_test('zxcxzc', 'qwewdasdasdasqe')


# def dec(func):
#     def wrapper(*args):
#         print('__________________')
#         func()
#         print('__________________')
#     return wrapper
#
from functools import wraps
def dec1(func):

    @wraps(func)
    def wrapper(*args):
        print('*****************')
        func()
        print('*****************')
    return wrapper

#@dec
@dec1
def hello_world():
    print("hello world")

print(hello_world.__wrapped__)

#
# result = dec(dec1(hello_world))()
#
# hello_world()
