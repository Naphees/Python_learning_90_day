# condition block
# if  condition true then if statement block execute
a = 10
if(a > 12):
    print(f"{a} is greater 2")
    # without parantheses
    if a > 10:
        print(a ,"grestest")
    # add more condition
    elif a > 15 and a  > 20:
        print(a,"is gretest from  15 , 20")
    elif a == 12 or a == 14:
        print(a, "equal 12 or 14 ")
    else:
        print(a)


# Short Hand if...else
a = 10
b = 15
bigger = a if a > b else b
print(bigger,"Bigger ")



# logical not  operator
print(not a > b) # True

# Nested if 
c = 40
if not c > 50:
    if(c < 30):
        print(c, "less than 30")
    elif c < 35:
        pass # add later
    else:
        print(c, "default condition")

# pass statement cannot be empty. but but if we
# for some reason have an if statement without no content


a = 10 
if a > 3:
    pass # add logic later

if a > 5:  # given error without pass
    pass



