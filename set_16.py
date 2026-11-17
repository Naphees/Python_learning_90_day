# Python Set
# Set is collenction is store diffrent data type value. but all item unique.
# Set items written in curly brackets.
#   its items unordered, unchange but we can add new item  
# and remove item
#  set not allow index

price = {1,3,4,2,5,1} # duplicate items not allow 1 remove automatic
print(price)

# True and 1 considered same value
# False and 0 consideded same value
price2 = {1,True,0,False}
print(price2)


# set length
print(len(price2))
# set store any data type
aSet = {1,3,4,5,True,False,"apple","banana"}

print(aSet)
# check data type
print(type(aSet))

# we can create set by set() constructor
bset = set((11,2,"3",2,2,3))# use double quotes
print(bset)


# Access Set Items
for x in bset:
    print(x)


# check items in set
print(3 in bset)


# change item not allow 

# Add item in set by add()
aset = {1,2,3,4}
aset.add(33)
print(aset)

# add item from another set 
bset = {1,33,44,55,66}
aset.update(bset)
print(aset)

# update method add dictionary , list , tuple 
list1 = ["List1","list2",22,2.2,0,0] # list
tuple1 = "aaple","banana",3333,333 # tuple
aset.update(list1)
aset.update(tuple1)
print(aset)