import random

name = input("your name: ")
choices = ["rock", "paper", "scissors"]

user_choice = input(f"Hi, {name} Enter your choice (rock, paper, or scissors): ").lower()
computer_choice = random.choice(choices)

print("Computer's choice:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print(f"You win!{name}")
else:
    
    print("Computer wins!")
    
