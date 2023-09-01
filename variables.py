# Lets play with variables
x = 23  # integer
y = True  # bool
z = 23.0  # double

j = 45  # integer
k = False  # bool
l = 12.3  # double

print(x + j)  # 68
print(y & k)  # False
print(z - l)  # 10.7

# In order to find the type of a variable we use type function
print(type(k))

# Working with string
fname = "Muhammad"
lname = "Rameez"

print(fname + " " + lname)  # Muhammad Rameez

# String Indexing
print(fname[0])  # M
print(lname[4])  # e

# String Range Indexing
print(fname[2:])  # hammad
print(fname[0:1] + lname[3:])  # Meez

# String Transformation
print(lname.capitalize())
print(fname.lower())

# date time in python
from datetime import date #import library
print(date.today()) #2023-09-01

