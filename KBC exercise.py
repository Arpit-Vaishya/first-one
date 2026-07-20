print(" Welcome to todays quiz ")
questions=[
["What is capital of india? ","delhi","mumbai","lucknow","banglore","none",1],
["What is the capital of germany?","helsnki","berlin","tokyo","denver","none",2],
["What is the capital of spain?","helsnki","denver","real madrid","argentina","none",3],
["BMW is from which country","india","germany","spain","Europe","none",2],
["Who is the ruling party in india?","BJP","CJP","AAP","CONGRESS","none",1],
["What is the brain of the computer?","motherboard","CPU","printer","moniter","none",2],
["Which tree gives maximum amount of oxygen?","neem","mongo","sapling","banyan","none",4],
["How long is 1 latha?","8.3 ft","1.3 ft","1.0 ft","8.5 ft","none",1],
["How many states are there in india?","28","30","29","31","none",1],
["How many union territories are there in india?","8","7","9","6","none",1],
["Which festival is known as festival of lights? ","holi","navratri","diwali","dahi handi","none",3],
["which currency is used for transcition globally?","yaun","rupee","euro","dollar","none",5],
]
level=[1000,2000,3000,5000,7000,9000,10000,30000,70000,100000,500000,1000000]
money=0
for i in range(0,len(questions)):

    question=questions[i]
    print(f"\n\n Question for rupees {level[i]} is \n {question[0]}")
    print(f"A.{question[1]} B.{question[2]}")
    print(f"C.{question[3]} D.{question[4]}\n")
    reply=int(input("Enter your answer in(1-4) or 0 to quit : "))
    if reply==0:
        money=level[i-1]
        break
    if reply==question[-1]:
        print(f"Your answer is correct, you have the won Rs.{level[i]}")
        if i==4:
            money=5000
        elif i==9:
            money=70000
        elif i==12:
            money=1000000
    else:
        print("Wrong answer!")
        break

print(f"\nThe money you take home is Rs.{money}")

        


