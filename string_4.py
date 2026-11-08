a = "Hello" # double quotes
b = 'Hello Dear' # single quotes
print(a)
print(b)

# Multi line sting
a = """
this 
is multi line string

"""
print(a)


# find specific character of string variable
b = "hello"
print(b[0],b[1])

# string with loop
for x in b:
   {
     print(x)  
   } 

for y in "lovely":
    print(y)


# find string length
a = "lovely string"
print(len(a)) # len()


# Check phrase or character in string
print('lovel' in a) # return true or false
if "v" in a:
    print("Yes , v present")


# check phrase or character not in string
print("a" not in a); # return true or false
