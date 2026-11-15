# tuple 
# tuple  declared by () parantheses
#  tuple item not changle directly , not replace, items ordered . not delete directly 
# it store any data type like int,float, string, boolean ect.
t1 = (1,2,4)
print(t1)

# second way declare tuple
t2 = 1,3,"apple",True,False,4.5
print(t2)

# tuple length
print(f"tuple length {len(t2)}")
print(f"tuple data type : {type(t2)}")

# declare empty tuple
t3 = ()
print(type(t3))

# declare tuple with an items with comma(,) otherwise not allow tuple
t4 = ("apple")# not tuple it is string
print(t4)
print(type(t4))

# single tuple elemment with comma
t4 = ("apple",)
print(t4)
print(type(t4))

# access tuple items
print(t1[0])# first items
print(t1[-1])# last items
# access range of item
print(t1[0:2])

# access all item by loop
for x in t1:
    print(x)

# check items exist in tuple
if 1 in t1:
    print(f"{1} is exist in {t1}")

# check items not exist in tuple
if 5 not in t1:
    print(f"{5} not exist in {t1}")