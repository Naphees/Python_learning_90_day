x = 5
y = "Sigma"

# Casting
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0
print(x,y,z)

# Get the type() function
x = 5
y = "Alfa"
print(type(x))
print(type(y))

# many values to multiple variables
x,y,z = 10 ,20 ,30
print(x,y,z)

# one value to multiple variables
x = y = z = "lovely"
print(x,y,z)

# Unpack a  collection
fruits = ["apple", "orange","cherry","banana"]
v,x,y,z = fruits
print(v,x,y,z)
print(fruits)

# output variable
x = 10
y = 20
print(x,y)

# use + operator 
x = "hello"
y = "lovey"
print(x + y)

# Global variables
x = 10 # Global variable
def myfunc():
    # access global variable
    print(x)

myfunc()

# global varible and local variable with same name
x = "Simga" # global
def myfunc():
    x = "Alfa" # local with same name
    print(x)

myfunc()
print(x)

# global keyword inside function
def myfunc():
    global x 
    x = "Alfa beta"

myfunc()
print(x)

