# List Remove Operations

list1 = [1,3,4,5]
print("List Operations")
print(list1)
# remove 3 
list1.remove(3)
print(list1)

# remove specific index
list1.pop(1)
print(list1)
list1.extend([3,4,5,5])
print(list1)

# remove element by del 
del list1[0]
print(list1)

# do empty list
list1.clear()
print(list1)

# delete list
#del list1
print(list1)




# Python Loop list
print("Python Loop List")

list1 = [1,2,3,4]
for x in list1:
    print(x)


# loop through with index
print("Loop through with index")
for x in range(len(list1)):
    print(list1[x])

# using with while loop
print("Using while loop")
i = 0
while i < len(list1):
    print(list1[i])
    i +=1

# List Comprehension:
# List Comprehension is shourt-cut  for list.

# example
print("List Comprehension")
list2 = [1,2,3,4,5]
[print(x) for x in list2]

# create new list
oldlist = ["apple","banana","kivi","orange"]
print(f"Old List: {oldlist}")
newlist =[]
for x in oldlist:
    if "b" in x:
        newlist.append(x)
 
print(f"New List: {newlist}")

# Second Approach
newlist = [x for x in oldlist if "b" in x]
print(newlist)

# Iterrable
newlist  = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10)if x <= 5]
print(newlist)

newlist = ["lovely" for x  in range(10) if x < 5]
print(newlist)

