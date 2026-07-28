import random
choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(choices)

user_choice=(input("Enter your choice (rock, paper, scissors): ")).lower()

# for user_choice in ["0"]:
#     print("Game Over")
#     break

if user_choice == computer_choice:
    print(f"It's a tie! Both chose {computer_choice}")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print(f"You win! You chose {user_choice} and the computer chose {computer_choice}")
else: 
    print(f"You lose! You chose {user_choice} and the computer chose {computer_choice}")





