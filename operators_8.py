# Topic  : Python Operators - Ternary, Comparision, Logical
# Day : 8 
# Date : 9.11.2026

# Ternary Operator
num = 6 
x = "Weekend" if num > 3 else  "Working"
print(x)

# Comparision operators
x = 5 
y = 3
print(x == y) # False
print(x != y) # True
print(x > y) # True
print(x < y) # False
print(x >= y) # True
print(x <= y) # False


# Chaining Comparisons
x = 5
print(1 < x < 18) # True
print(1 < x and x < 6) # True


# Logical Operators
# Logical and 
x = 5
y = 3
if x > y and y > 2 :
    print("Both condition are true")

# Logical or
if x < y  or  x > 3 : 
    print("True, One condition True")
# Logical not "Reverse the result"

print(not (x > y)) # False