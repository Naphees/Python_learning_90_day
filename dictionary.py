
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":2000
}
print(thisdict)

# print specific  key
print(thisdict["brand"])


# length of dictionary
print(len(thisdict))


# Dictionary Items - Data Types

cars = {
    "brand":"Ford", # String
    "electric":False, # Boolean
    "year":2000, # integer
    "colors":["red","white","blue","black"],#list
    "price":30000000.45 ,# float
   # "price":3.4
}
print(cars)

# Dictionary Data type
print(type(cars))


# dict() Constructor
## make dictionary
dev =  dict(name="Alfa",age=24,country="Norway")
print(dev)


# dictionary() items access

cars = {
    "Brand":"Tata",
    "Model":"Range Rower",
    "Year":2000
}

# 1 . 
print(cars["Brand"])

#  2. by get() function
print(cars.get("Brand"))

# 3. get all keys
print(cars.keys())

# 4. get all values
print(cars.values())
# 5. get items
print(cars.items())

# 6. Check key exist or not
if "Model" in cars:
    print("Yes, 'Model' is exists")
