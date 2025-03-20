thisdict= {
    "year":"2076",
    "exam":"slc",

}
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x=thisdict["model"]
print(x)#accessing the data in dictionary
y=thisdict.keys()
print(y)
z=thisdict.values()
print(z)
a=thisdict.items()
print(a)

#changing the data in a dictionary
dict ={
    "house":"villa",
    "color":"red",
    "floors":"3"
   }
dict["location"]="kupondole"
print(dict)
dict.update({"backyard":"yes"})
print(dict)
#removing the items
dict.pop("color")
print(dict)
dict.popitem()
print(dict)
for x in dict.values():
    print(x)