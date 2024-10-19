def bubble_sort(_list):
    for i in range(len(_list) - 1):
        for j in range(len(_list) - i - 1):
            if _list[j] > _list[j + 1]:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
    return _list


a = [1, 10, 8, 3, 7, 19, 3, 6]
print(bubble_sort(a))
