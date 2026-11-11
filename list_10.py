# List in is collection is python
# store any data type,
# can change elements , delete
#  allow duplicate value
# list items ordered
# list  created by  []
# list first index is [0]
# list  negative index start from end

# example
print("List Practice")
list1 = ["apple", "banana", "banana", 1,3,4,4,4.5,True]
print(list1)

# find second elememt
print(list1[1])
# last element
print(list1[-1])

# list length
print(len(list1))

# list check Data type
print(type(list1))

# list created by list() constructor
list2 = list(("apple","banana"))
print(list2)

# access list items by range
list3 = [1,2,3,4,4,5,6,7]
print(list3[1:5]) # 2,3,4,4
print(list3[2:]) # access all element from 2 index
print(list3[-3:])# 5,6,7

