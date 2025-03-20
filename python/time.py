import time

# Get the current time
current_time = time.strftime('%H:%M:%S')
print("Current Time:", current_time)

# Get the current hour, minute, and second
current_hour = int(time.strftime('%H'))
current_min = time.strftime('%M')
current_sec = time.strftime('%S')

print("Current Hour:", current_hour)
print("Current Minute:", current_min)
print("Current Second:", current_sec)

# Print greeting based on the current hour
if 4 <= current_hour < 12:
    print("Good Morning!")
elif 12 <= current_hour < 18:
    print("Good Afternoon!")
elif 18 <= current_hour < 24:
    print("Good Evening!")
else:
    print("Good Night!")
