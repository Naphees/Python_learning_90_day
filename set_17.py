# Python Set
# remove set items
# by remove() or discard() method
# remove() return error when  item not present  in set
aset = {1,2,3,4}
aset.remove(1) # if remove item not found give an error
print(aset)
 # notice this aset.remove(5)
print(aset)

# discard()  not return error when item not present in set
aset.discard(3)
aset.discard(5) # Notice : 5 not present in set
print(aset)

# add new items in set
aset.add(3)
aset.update({4,5,5,44})

print(aset)
# remove randomly by pop() method
aset.pop()
print(aset)


# clear() empties set
aset.clear()
print(aset)

# del keyword will delete  set completely
del aset
#print(aset)# genrate error