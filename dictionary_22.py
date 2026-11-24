# Nested dictionary in python

products = {
    "product1":{
        "name":"Jease",
        "price": 2000
    },
    "product2":{
        "name":"Belt",
        "price":500
    },
    "product3":{
        "name":"Shoes",
        "price":1600

    }
}
'''
Access Dictionary
items
'''
print(products)

"""
 Add dictionaries into a  dictionary

"""
student1 ={"name":"Sigma"}
student2 = {"name":"Alfa"}

students = {
    "first":student1,
    "second":student2
}
print(students)

# print second student name
print(students["second"]["name"])

