mylist = ['a','b','c','d','e','f','g','h','i','j','k','l','m']

print(mylist)
print(mylist[5])
print(mylist[1:9])

# Methods of list
mylist.append('n') # append adds the element at the last
print(mylist)
mylist.insert(1,'A') # insert helps to add element at any specified index(index,element)
print(mylist) 
popped = mylist.pop(1) # it pops the given index element
print(mylist)
print(popped)

# Nested list  
ls1 = [1,2,3]
ls2 = [4,5,6]
ls3 = [7,8,9]
mega_list = [ls1,ls2,ls3]
print(mega_list)
print(len(mega_list))
print(mega_list[2])
print(mega_list[2][1])