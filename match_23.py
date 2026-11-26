# Python match
# The match statement is used to perform different actions
# based on different conditions

# The match statement selects one of many code blocks to 
# be executed

day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")


# match with default value
day = 14
match day:
    case 1| 2| 3| 4|5:
        print("working day")
    case 6 | 7 | 8 | 9:
        print("Traveling day")
    case _:
        print("Case not match")