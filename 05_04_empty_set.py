#this will create an empty dictionary and not an empty set
a= {}
print(type(a))

#this will create an empty set

b= set()
print(type(b))
b.add(4)
b.add(5)
b.add(5)  #this repeated value will not be added
# b.add([1,2,3]) #this will give error because you can't add list into a set
# b.add((1,2,3)) #you can add tuple into a set

# print(len(b)) #prints the length
# b.remove(5)
# b.pop()
# b.clear() #empties the set
# print(b)

#b.union({5,4})
b.intersection({5,4})
print(b)