from random import randint


def get_unique_list_numbers() -> list[int]:
    start = -10
    stop = 10
    width = 15
    list_ = []
    while len(list_) < width:
        num = randint(start, stop)
        if num not in list_:
            list_.append(num)

    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
