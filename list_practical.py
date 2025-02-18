# empty list
list1 = []

# list with value
list2 = [1,2,3,4,3,3,3,3,3,3]
print(list2)

# slicing a list in python
print(list2[1:2])

# count
print(list2.count(3))

# index
print(list2.index(4))

# insert
list2.insert(10,11)
print(list2)

# pop - delete
list2.pop(4)
print(list2)

# extend
list3 = ["abc","cvb"]

list2.extend(list3)
print(list2) 

# copy

list4 = list2[:]
list5 = list4.copy()
print(list4)
print(list5)

#  sort 
list6 = [1,4,6,8,0,3,4,5,3]
list6.sort(reverse=True)
list6.sort()
print(list6)

# list comprehension
list6 = [i for i in range(10) if i%2 == 0]
a = [word for word in list6 if word.startswith("a")]
print(a)


