print("The game starts\n" \
"play and earn ")
questions=[" 1. What is the capital of india? \n ",\
           " 2. Berlin is in which country? \n",\
            " 3. Which drink Indians love most to have in their breakfast? \n",\
            " 4. What are the 5 basic needs of the Humans? \n",\
            " 5. What does every person wants in his/her life? \n"]

for q in questions:
    print(q)



answers=(" Dehli"," Germany"," Tea"," Food , Water , Shelter , Sleep , Clothes"," Peace")

print("The correct answers of the given questions are as follows : \n  a")

for a in answers:
    print(a)

a=int(input("So what was your score out of 5? =\n"))

if a==5:
    print("You are the goat of the contest \n CONGRATULATIONS!! \n You won your 1 crore \n HURAHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
elif a==4:
    print("You have the nice IQ \n CONGRATULATIONS!! \n You won your 75 lakhs \n HURAHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
elif a==3:
    print("You have the good IQ \n CONGRATULATIONS!! \n You won your 59 lakhs \n HURAHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
elif a==2:
    print("You have the beloew Average IQ \n CONGRATULATIONS!! \n You won your 30 lakhs \n HURAHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
elif a==1:
    print("You have the lowest IQ \n CONGRATULATIONS!! \n You won your 10 laks \n HURAHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
elif a==0:
    print("You have the worst IQ \n CONGRATULATIONS!! \n You lost in the game \n HURAHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
else :
    print("invaild input\n")

b=input("have you ever watched cartoons???????????????\n yes/no = \n")
if b=="yes":
    print("Great!!!!!!!!!!!!!!!")
else:
    print("youv are biggest dumbass fool!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")