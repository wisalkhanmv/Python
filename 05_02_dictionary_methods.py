myDict = {
    "fast": "in a quick manner",
    "wisal": "co-founder of abwisk",
    "marks" : [1,2,4],
    "anotherDict" : {"zn":"tn"} ,#dictionary witin dictionary
    1:2
}
# print(myDict.keys())    #print keys
# print(myDict.values())  #print values
# print(myDict.items())   #print (key, value) of the dictionary
# print(type(myDict.keys()))
# print(list(myDict.keys()))

updateDict = {
    "tn":"you",
    "wisal":"the actual co founder of abwisk"
}
myDict.update(updateDict)
print(myDict.get("wisal")) #if wisal is not in dict then it'll print null
print(myDict["wisal"]) #will print error if wisal is not in dict