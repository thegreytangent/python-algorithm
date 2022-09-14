def insertion_sort(_list):
	for i in range(1, len(_list)): #1,2,3,4
		print(i)
		val = _list[i]
		while i > 0 and _list[i-1] > val:
			_list[i] = _list[i-1]
			i = i - 1
		_list[i] = val
	return _list

sort = insertion_sort([6,5,8,2,3]);

print(sort)