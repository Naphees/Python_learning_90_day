# Change items in list
list1 = [1,2,3]

# change item by index first index is [0]
# replace 2 from 5
print("List Items practice")
print(f"Pre list : {list1}")
list1[1] = 5
print(list1)

# change by range
list2 = [1,2,3,4,5]
list2[1:3] =[1]
print(list2)


# insert item at specific  index by insert method 
list3 = [1,2,3]
list3.insert(1,44)
print(list3)


# add item in  list by append()
list3.append(22)
print(list3)

# add items of another list in  list by extend()
list4 = [2,22,33,44,55]
list3.extend(list4)
print(list3)

# we can add ruple, set, dictionary by extend()
tuple1 = (1,3,4,5)
list3.extend(tuple1)
print(list3)