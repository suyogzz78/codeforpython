#break skips the loop it lies in
'''for i in range (1,11):
    print("4 *",i,"=",4 * (i))
    if (i==7):#when i=7,it terminates the loop as there is a break statement
     break

print("skip the loop")'''

#continue skips the iteration
for i in range (1,11):
  
    if (i==7):
     print("skip the loop")
     continue
    

    print("4 *",i,"=",4 * (i))
