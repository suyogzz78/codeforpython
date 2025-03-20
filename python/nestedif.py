n=int(input("enter a number :"))
print("your number is :",n)
if(n<0):
    print("the number is negative ")
elif(n>0):
    if(n<=10):
        print("the number is between 1-10")
    elif(n > 10 and n<=30):
        print("the number is between 11-30")
    else:
        print("the number is greater then 30")
 
else:
    print("the number is 0")