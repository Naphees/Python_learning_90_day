# Dictionary items
# Update items in dictionary 

s = {
    "a":"sigma",
    "b":"beta"
}
# update sigma  into alfa
s["a"] = "alfa"
print(s)

# update item by update()
s.update({"a":"Hello"})
print(s)

# Add item in dictionary
s["c"]= "good Job"
print(s)

# by update method
s.update({"d":"Ok update() method"})
print(s)

# Remove items
# first pop() method
# remove specific item by key
s.pop("a")
print(s)

# remove last items by popitem()
s.popitem()
print(s)
# remove item by del keyword
del s["b"]
print(s)
s["cc"] = "Welcome"
print(f"Add item ${s}")
# empty  dictionary by clear()
s.clear()
print(f"Empty dicionary {s}")

# remove dictionary by del keyword
del s
# print(s) now genrate error


# Loop Through a dictionary
# use for loop
student = {
    "name":"Sigma",
    "age":20,
    "MCA":True,

}

# print all keys
for x in student:
    print(x)

# print all values
for x in student:
    print(student[x])

# print values by values()
for x in student.values():
    print(x)

# print all keys by keys()
for x in student.keys():
    print(x)

# Loop through both keys and values by itmes()
for x,y in student.items():
    print(x, " : " ,y)


# Copy dictionary 
# copy dictionary by copy() method
student1 = student.copy()
print(student1)

# copy dictionary by dict() method
student3 =  dict(student)
print(student3)