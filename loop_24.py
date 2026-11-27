# Python Loops
#. while ,for

print("while loop")
i = 0
while i < 6:
    print(i)
    i += 1
print("break keyword")
# break keyword in loop
i = 1
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1

# continue keyword
print("continue keyword")
i = 1
while i < 10:
 if i == 4:
    i += 1
    continue
 print(i)
 i += 1


# Else statement in  while loop
i = 1
while i < 4:
   print(i)
   i += 1
else:
   print("Finished loop")

# else with break keyowrd
i = 1 
while i < 4:
   print(i)
   if i == 2:
      break
   i += 1
else:
   print("Finished loop")

# for loop
fruits = ["apple","banana"]
print("for loop")
for x  in fruits:
   print(x)


# range() function use in loop . 
# default start with 0 
# default increase with 1
for x in range(5):
   print(x)
else:
   print("5 exclude")

# two parameters in range
for x in range(2,5): # 5 exclude
   print(x)

# incrase value self pass 3 parameters 
# first starting
# second <  last point
# increse value
for x in range(2,10,3):
   print(x)