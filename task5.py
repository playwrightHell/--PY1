import random


def get_random_password() -> str:
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b = 'abcdefghijklmnopqrstuvwxyz'
    c = '0123456789'
    password = random.sample(a + b + c, 8)

    return password


print(get_random_password())
