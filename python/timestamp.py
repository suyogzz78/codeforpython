import time
currenttime=time.strftime('%H:%M:%S')
print(currenttime)
currenthour=int(time.strftime('%H'))
print(currenthour)
currentmin=time.strftime('%M')
print(currentmin)
currentsec=time.strftime('%S')
print(currentsec)
#if( 4 <= currenthour <12):
  #  print("goodmorning")
#else:
   # print("goodafternoon")

if(currenthour>=0 and currenthour<  12):
    print("good morning sir!")
elif(currenthour>=12 and currenthour<17):
    print("goodafternoon")
if(currenthour>=17 and currenthour<0):
    print("goodnight")

   