
print("Welcome to the Jungle Adventure")


choice = input("Do you want to go left or right? ").lower()

if choice == "right":
    print("Game Over")
elif choice == "left":
    
    action = input("Do you want to climb a tree or explore th caveve? ").lower()

    if action == "climb a tree":
        print("Game Over")
    elif action == "explore the cave":
    
        creature = input("Choose between bear, tiger, or snake: ").lower()

        if creature == "bear" or creature == "tiger":
            print("Game Over")
        elif creature == "snake":
            print("You win!")
        else:
            print("Invalid choice. Game Over.")
    else:
        print("Invalid action. Game Over.")
else:
    print("Invalid choice. Game Over.")
