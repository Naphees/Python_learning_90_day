# join two sets

#  Symmetric_difference() method keep only the elements that are not
# present in both sets
aset = {1,2,3}
bset = {2,3,3,5,6}
cset = aset.symmetric_difference(bset)
print(cset)

#  we can use ^ operator  same result but use with only set data type
cset = aset ^ bset
print(cset)

# symmetric_diffrence_update() same as symmetric_difference() but not return new set
aset.symmetric_difference_update(bset)
print(aset)


# Frozenset :is immutable version of a set
# like sets it contains unique,unordered,unchangeble,elements
# unlike set elements cannot be  added or removed from the frozen set

# use frozenset() constructor  to create frozenset, 
# from any uterable

x = frozenset({"aa","apple",3,3,44})
print('frozenset')
print(x)
print(type(x))

# frozenset support all set set methods
cp = x.copy()
print(cp)