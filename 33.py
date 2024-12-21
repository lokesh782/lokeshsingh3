
print("Welcome to the Haunted House")
choice = input("Do you want to go upstairs or downstairs? ").lower()

if choice == "downstairs":
    print("Game Over")
elif choice == "upstairs":
    
    action = input("Do you want to enter the room or stay outside? ").lower()

    if action == "enter the room":
        print("Game Over")
    elif action == "stay outside":
        
        creature = input("Choose between ghost, vampire, or werewolf: ").lower()

        if creature == "ghost" or creature == "vampire":
            print("Game Over")
        elif creature == "werewolf":
            print("You win!")
        else:
            print("Invalid choice. Game Over.")
    else:
        print("Invalid action. Game Over.")
else:
    print("Invalid choice. Game Over.")
