# Python Function
# declared by def keyword
def hello():
    print("first fun")

# call function
hello()

# function name rule: start with letter or underscore
# contain numbers , letters, and _
# function name case sensitive

""" 
it genrate error
def 1div():
print("hello")

"""
# function parameters and aguments
def hello(name): # parameter  (postional)
    print(name)
hello("Sigma") # arguments

# optional arguments
def hello(name = "sigma"):
    print(name)
hello("Alfa")
hello()

# keyword arguments
def hello(name, role):
    print(name, role)
hello(name="Alfa",role="Developer")

# return keyword same as javascript
# pass used empty placeholder

def hello():
   return  2
result = hello()
print(result)

# we pass  anydata type as an argument

# allow only keyword arugments
# use / in last
def hello(name, /):
    print(name)
hello("King")

# allow only keyword argument
# use * in starting
def hello(*,name):
    print(name)
hello(name="keyword argument allow")

# Combining Positional only and keyword only argment
# first declare postional agruments
def add(a,b,/,*,c,d):
    return a+b+c+d
print(add(4,3,c=4,d=3))

