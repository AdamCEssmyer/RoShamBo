import random

user_action = input("Enter a choice (ro, sham, bo): ")
possible_actions = ["ro", "sham", "bo"]
computer_action = random.choice(possible_actions)

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "Ro":
    if computer_action == "Bo":
        print("Ro smashes Bo! You win!")
    else:
            print("Sham covers Ro! You lose.")
elif user_action == "sham":
    if computer_action == "ro":
            print("sham covers ro! You win!")
    else:
            print("Bo cuts sham! You lose.")
elif user_action == "Bo":
    if computer_action == "sham":
        print("Bo cuts sham! You win!")
    else:
            print("Ro smashes Bo! You lose.")
