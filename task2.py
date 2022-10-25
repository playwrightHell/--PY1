str_dict = {}


def get_count_char(str_):
    str_ = "".join(str_.lower().split())
    for word in str_:
        if word.isalpha() is True and word in str_dict:
            str_dict[word] += 1
        elif word.isalpha() is True and word not in str_dict:
            str_dict[word] = 1
    return str_dict


def symbols(s_dict):
    sum_ = sum(s_dict.values())
    for i in s_dict:
        s_dict[i] = round(s_dict[i] / sum_ * 100, 1)
    return s_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
