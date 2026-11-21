# Python Dictionary
# Are used to store data values, in key : value pairs
# A dictionary is collection which is ordered* , changeble and do not
# allow duplicate values.
# written with curly brackets.
# store any data type

a = {
    "brand":"Sigma",
    "model":"Mustang",
    "year":2000,
    "color":["red","green","blue"],
    "owner":{"simga","alfa","beta"},
    "electric":True,
    "year":2026 # duplicate key
}
# print dictionary
print(a)
# access dictionary items
print(a["color"])
# access by get method
print(a.get("owner"))

# dictionary length
print(len(a))
# check data type
print(type(a))

# create dictionary with dict() constroctor
b = dict(name="Alfa",age=26, educated=True)
print(b)

# find the keys in dictionary
print(a.keys())

# find the values in dictionary
print(a.values())

# find items with key and values
print(a.items())

# check key exist in dictionary
if "brand" in a:
    print("Yes")

# check key not exist in dinctionary
if "name" not in a:
    print("Not Exist")