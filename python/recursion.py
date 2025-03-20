#recursion is process of defininf something itself
#basically calling a function itself
'''def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return(n*factorial(n-1))#recursive function
    
n= int(input("enter the number you want the factorial of: "))
print("factorial is ",factorial(n))

'''
def fibo(n):
    if n<=0:
        print("enter a positive number ")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
n=int(input("enter a number you want the fibo series of "))
print ("the fibo  is ",fibo(n))

        
