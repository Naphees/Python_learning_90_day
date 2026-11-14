# list Sort
list1 = ["apple","banana", "manngo","kivi"]
list1.sort()
print(list1)

list2 = [1,3,2,3,4,5]
list2.sort(reverse= True)
print(f"List reverse order {list2}")

# default sort is case sensitive
list1 = ["apple","banana","Apple","Banana"]
list1.sort()
print(f"Case Sensitive {list1}")
list1.sort(key=str.lower)
print(f"Case Insentive Sort {list1}")


# Join Two List
list1 = [1,2,3]
list2 = [3,4,5]
list3 = list1 + list2
print("Join Two List")
print(list3)

# join list with append method
for x in list1:
    list2.append(x)
print(f"Join list by append method {list2}")

# join by extend()
list1.extend(list2)
print(f"join list by extend method {list1}")


# List Copy 
print("list copy")
list1 = [1,2,3,4]
list2 = list1.copy()
print(list2)

print("copy list by list() method")
list3  = list(list2)
print(list3)

print("list copy by slice(:) operator")
list4 =list3[:]
print(list4)
