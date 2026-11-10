#  Identity Operator , 
# is  , is not
# used for object
x = ["apple", "banana"]
y = ["apple", "banana"]

print("Indentity Operators")

print(x is y) # False because check value and memory location
print(x == y) # True because check value

z = x 

print(x is z) # True , because same memory location, and value
print(x is not y) # True , because same value but not same location
print(x is not z) # False, because same value and same location

# Membership Operators 
# It checks sequence in object
# in, not in

print("Membership operators")
course =["Mern","Php","Python"]
print("Mern" in course) # True

print("C" in course) # False

print("C" not in course) # True , not in course


# Bitwise Operators
# Bitwise operators are used to compare (binary) numbers
print("Bitwise Operators")
# & = And operation , return 1 if both bits is 1
print(5 & 3) # 5 = 101, 3 = 011 , return  1

# | = Or operator, return 1 if any one bit 1 in both

print(5 | 3) # 5 = 101, 3 = 011, return 7 binary is 111

# ^ = XOR operator,return 1 if one bit 1 in both 
print(5 ^ 3) # 5 = 101, 3 = 011, return 6 

# ~ = NOT operator, Invert all bits
print(~3) # 3 = 000000011 ,1111111100= return -4


# << = Left shift operator , shift bit left side
print(3 << 2) #  3 = 00011 shift 2 place all bits  return 01100  == 12

# >> right shift operator , shift bit right side
print(3 >> 2) # return 0
print(5 >> 2) # return 1