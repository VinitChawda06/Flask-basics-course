mystring = "abcdefghijklmnopqrstuvwxyz"
name = "Vinit"
flavour = "chocolate"

# Slicing [start:stop:step]
print(mystring[2])
print(mystring[2:8])
print(mystring[0:21:3])
print(mystring[::2]) # from start to end every 2 stepped element will be printed
print(mystring[::-1]) # reversed string

#Methods of string
print(mystring.upper())
print(mystring.lower())
print(mystring.split())
print(mystring.split('h')) # it will exclude h and create a new element in the list

# .format string use
## print("The favourite flavour of Vinit is chocolate") This can be written using .format as shown below
print("The favourite flavour of {} is {}".format(name,flavour))

# f formatted string
print(f"{name} loves {flavour}")