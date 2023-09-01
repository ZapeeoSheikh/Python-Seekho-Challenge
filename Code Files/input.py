fname = input("Enter your First Name: ")
lname = input("Enter your Last Name: ")

name = fname.capitalize() + " " + lname.capitalize()
print("My name is " + name)

a = 12 # integer

# With String interpolation you can only use String with String Variable
# But for using integer with string, we need to type cast first like str()
print("My name is " + str(name) )
print("My name is " + str(a) ) # Type cast is required
