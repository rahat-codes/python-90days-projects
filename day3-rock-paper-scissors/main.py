import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:

    user_choice = input("\nEnter rock, paper, scissors:  ").lower()

    if user_choice not in choices:
        print("❌ Invalid choice!")
        continue

    computer_choice  = random.choice(choices)

    print(f"💻 Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a draw!")
    
    elif(
        (user_choice == "rock" and computer_choice=="scissors") or
        (user_choice == "paper" and computer_choice=="rock") or
        (user_choice == "scissor" and computer_choice=="paper")
    ):
        print("🎉 You win!")
        user_score += 1
    
    else:
        print("😢 Computer Wins!")
        computer_score += 1

    print(f"\n📊 Score: ")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")


    play_again = input("\nPlay again? (yes/no): ").lower()

    if play_again !="yes":
        print("\nThanks for playing!")
        break