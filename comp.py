#Winston Venderbush
#Constantine Athanitis

def union(list1, list2):
	list3 = list1 + [x for x in list2 if x not in list1]
	return list3

def intersect(list1, list2):
	list3 = [x for x in list1 if x in list2]
	return list3

def difference(list1, list2):
	list3 = [x for x in list1 if x not in list2]
	return list3

def symdiff(list1, list2):
	list3 = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
	return list3

def cartprod(list1, list2):
	list3 = [(x, y) for x in list1 for y in list2]
	return list3

#print cartprod([1, 2, 3], [2, 3, 4])
#print cartprod([2, 3, 4], [1, 2, 3])