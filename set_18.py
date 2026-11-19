# Python Set

# Join Set 
# update and union method join two set

set1 = {1,2,3}
set2 = {3,4,5}
# union return new set
set3 = set1.union(set2)
print(set3)
#  we can use | operator  to join set . note | work only set not other data type
set3 = set1 | set2
print(set3)
# join another data type by |
list1 = [444,33,"list1"]
# set3 = set1 | list1 // not allow with |
set3 = set1.union(list1)


print(set3)

# update similar union, but update not return new set , change in exist set
set1.update(set3)
print(set1)


# intersection return new set with duplicate  elements
# insersection can work another data type like list ,tuple 
# we can also use & operaton only with sets not use with another data type

set1 = {1,2,3,False}
set2 = {3,4,3,"apple",True ,1,0}
set3 = set1.intersection(set2)
print(set3)
# False is 0 , True is 1
set3 = set1 & set2
print(set3)

tuple1 = [1,2,3,"apple", False, True]
# genrate error set3 = set1 & tuple1


set3 = set1.intersection(tuple1)
print(set3)

# intersection_update() similar same as instersection() ,but not return new set , change in first set

set1.intersection_update(tuple1)
print(set1)


# diffrence() will return new set that will contain only the items from the first set that are
# not present in the another set
# we can use "-" hyphen operator .allow only with set , not another data type
set1 = {1,2,3,0}
set2 = {3,4,5,False}
set3 = set1.difference(set2)
print(set3)

set3 = set1 - set2
print(set3)
list1 = [1,2,3,55,44]
#set3 = set1 - list1 it return error
set3 = set1.difference(list1)
print(set3)

# diffrence_update() same as differece() but not return new set  . It change in first set
set1.difference_update(list1)
print(set1)