a = int(input(" Enter 1st number : "))
b = int(input(" Enter 2nd number : "))
print("The numbers you havr chosen are : " , a , "and" , b )

print("+ , - , * , / ")

c = input("enter your choice from above : ")

match c:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _:
        print("invalid choice")





