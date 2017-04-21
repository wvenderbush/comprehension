#Winston Venderbush
#Constantine Athanitis

def union(list1, list2):
	list3 = [ x for x in list1 and y for y in list2 if y not in list2]
	return list3


print union([1, 2, 3], [2, 3, 4])