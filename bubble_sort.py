def bubble_sort(_list):
    index_len = len(_list) - 1;
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_len):
            if _list[i] > _list[i+1]:
                sorted = False;
                _list[i], _list[i+1] = _list[i+1],_list[i]
    return _list


print(bubble_sort([5,3,8,6,7,2]))   