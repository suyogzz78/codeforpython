#set method such as union,intersection etc...
s1={1,2,3,4,5}
s2={5,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

city1={"tokyo","kathmandu","new-delhi"}
city2={"melbourne","perth","sydney","amsterdam","new-delhi"}
city3=city1.union(city2)
print(city3)
city4=city1.intersection(city2)
c5=city1.symmetric_difference(city2)
print(c5)
c6=city2.difference(city1)
print(c6)