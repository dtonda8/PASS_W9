from data_structures.array_list import ArrayList
from data_structures.list_adt import List
from data_structures.linked_list import LinkedList
from data_structures.array_sorted_list import ArraySortedList

def AL(lst: List) -> ArrayList:
    res = ArrayList(len(lst))
    for num in lst:
        res.append(num)
    return res

def LL(lst: List) -> LinkedList:
    res = LinkedList()
    for i, num in enumerate(lst):
        res.insert(i, num)
    return res

def ALtoList(al: ArrayList):
    out = []
    for i in range(len(al)):
        out.append(al[i])
    return out

def LLtoList(ll: LinkedList):
    out = []
    for i in range(len(ll)):
        out.append(ll[i])
    return out

def SLtoList(sl: ArraySortedList):
    out = []
    for i in range(len(sl)):
        out.append(sl[i].value)
    return out