name=input("Enter your name:")

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

timestamp = int(time.strftime('%H'))

if timestamp<12:
    greeting= "GOOD MORNING"
elif 12<timestamp<17:
   greeting= "GOOD AFTERNOON"
elif  17<timestamp<22:
    greeting= "GOOD EVENING"
else:
    greeting= "GOOD NIGHT"

print( greeting ,name , "sir!!")
     
