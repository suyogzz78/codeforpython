#ifelse
a=200
b=300
if b > a:
    print("b is greater than a")


    #indentation means the whitespace at the beginning of the line to define the scope of the code
'''
a=200
b=300
if b > a:
print("b is greater than a")
else:
print("a is greater")'''
#this would be error 

#elif means to try new condition if the previous one are not true
a=400
b=300
if b > a:
    print("b is greater than a")
elif a > b:
    print("a is greater")

#else(it catches anything that is not caught by the preceding conditions)
a=200
b=200
if b > a:
    print("b is greater than a ")
elif a > b:
    print("a is greater")
else:
    print("a and b are equal ")

#short hand ifelse
a=2
b=60
print("a") if a > b else print("b")

a = 33
b = 200

if b > a:
  pass
