myDict = {
    "fast": "in a quick manner",
    "wisal": "co-founder of abwisk",
    "marks" : [1,2,4],
    "anotherDict" : {"zn":"tn"} #dictionary witin dictionary
}
print(myDict['fast'])
print(myDict['wisal'])
myDict['marks']= [2,44,3]
print(myDict['marks'])
print(myDict["anotherDict"]['zn'])