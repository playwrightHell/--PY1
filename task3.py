def delete(list_, index=None):
    if index is not None:
        a = list_[:index]
        b = list_[index+1:]
        end_ = a + b
        return end_
    else:
        return list_[:-1]


print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
