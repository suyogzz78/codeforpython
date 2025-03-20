"""#set is collection of well defined objects
a={4,78,5.5,"suyog"}

for value in a:
    print(type(a))"""

thisset = {"apple", "banana", "cherry", True, 1, 2}#here it assumes true and 1 are same so it ignores one of them
print(thisset)
#to find length of the set
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(len(thisset))
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
set4 = {"abc", 34, True, 40, "male"}#set with integers,boolean and strings
print(set4) 

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#accessing sest items
thisset={"apple","banana","cherry"}
for x in thisset:
    print(x)

    thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
#adding set items
thisset={"ferari","lambo"}
thisset.add("ford")
print(thisset)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

theset={"banana","apple","orange"}
theset.remove("banana")
print(theset)
theset={"banana","apple","orange"}
theset.discard("banana")
print(theset)
thesset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#loop items
set={"ab","virat","gayle"}
for x in set:
     print(x)
     set1 = {"a", "b", "c"}

set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)