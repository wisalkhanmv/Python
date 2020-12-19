dictionary = {
    "End" : "Khatam",
    "Start" : "shoro",
    "Middle" : "Darmeyan"
}
print("options are:" , dictionary.keys())
a= input("enter a word : ")

#the below line will give error if the key is not present
#print("the meaning is :", dictionary[a])

#the below line will not give error if the key is not present
print("the meaning is :", dictionary.get(a))
