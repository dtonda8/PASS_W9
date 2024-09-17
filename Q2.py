from typing import List
from data_structures.referential_array import ArrayR

def merge(list1: List[int], list2: List[int]) -> ArrayR[int]:
	res = ArrayR(len(list1) + len(list2))
	return merge_aux(list1, list2, 0, 0, res, 0)
	# raise NotImplementedError()

def merge_aux(list1, list2, i1, i2, res, res_idx):
	if i1 == len(list1): # all elements of list1 added
		for i in range(i2, len(list2)):
			res[res_idx] = list2[i]
			res_idx += 1
		return res

	if i2 == len(list2): # all elements of list2 added
		for i in range(i1, len(list1)):
			res[res_idx] = list1[i]
			res_idx += 1
		return res
	
	if list1[i1] <= list2[i2]:
		res[res_idx] = list1[i1]
		return merge_aux(list1, list2, i1+1, i2, res, res_idx + 1)
	else:
		res[res_idx] = list2[i2]
		return merge_aux(list1, list2, i1, i2+1, res, res_idx + 1)

if __name__ == "__main__":
	pass