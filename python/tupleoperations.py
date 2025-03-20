num=(1,2,3,4,5)
print(type(num))
temp=list(num)
temp.append(6)
num=tuple(temp)
print(num)
#concatenating the numbers
num1=(1,2,3,4,5)
num2=(6,7,8,9,10)
num= num1+num2
print(num)
#counting
tuple1=(1,2,3,4,5,3,3,3,3)
counting=tuple1.count(3)
indexing=tuple1.index(4,4) 
print(counting)
print(indexing)

