# tuple update

# not directly update tuple, first convert turple into list
# then update list , after convert list into tuple
# We can do all operations of list
tuple1 = (1,3,4,4)
list1 = list(tuple1)

print(f"Tuple Update Practice: {tuple1} ")

# add items
list1.append(44)
# remove itmes from tuple 
list1.remove(1)
tuple1 = tuple(list1)
print(f"Added items in in last {tuple1}")


# Unpacking Tuple
fruits = ("apple","banana","mango","kivy")
(a,b,c,d) = fruits
print(a,b,c,d)
(a, *b, c) = fruits

print(f"{a,b,c}")

# Join tuple
t1 = (1,34,4)
t2 = 3,4,5
t3 =t2 + t1
print(t3)

# multiple 2 in tuple
tt = 1,2,3,4
tt = tt * 2
print(tt)
# multiple 4 in tuple
tt = tt * 4
print(tt)

