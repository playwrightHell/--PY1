from pprint import pprint

dict_list = []

for i in range(16):
    num = {}
    num["dec"] = i
    num["bin"] = bin(i)
    num["oct"] = oct(i)
    num["hex"] = hex(i)

    dict_list.append(num)

pprint(dict_list)
