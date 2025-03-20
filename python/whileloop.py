'''players = ['ronaldo', 'messi', 'neymar', 'suarez']
i = 0
while i < len(players):
    print(players[i])
    i += 1'''
i=5
while(i > 0):
 print(i)
 i=i-1
else:
 print("shit")
  
  #simple while loop
 i=1
 while i < 6:
  print(i)
  i+=1


#break the loop
i=1
while i < 6:
 print(i)
 if i == 3:
  break
 i+=1
    
i=0
while i < 6:
 i+=1
 if i==3:
  continue
 print(i)

 i=1
 while i < 6:
  print("*")
  i+=1
else:
 print("i is no longer less than 6")

def print_star_pattern():
    star_count = 5
    while star_count > 0:
        print('*' * star_count)
        star_count -= 1

print_star_pattern()

def print_star():
  star=1
  while star <= 5:
    print('*'*star)
    star +=1
print_star()

i=2
while i< 7:
  print(i)
  if i==3:
   break 
  i+=1


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

fruits=["apple","banana","cherry"]
for x in fruits:
  print(x)

houses=["house","villa"]
for x in houses:
  if x== "house":
    break
  print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(2, 30):
  print(x)

  adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)