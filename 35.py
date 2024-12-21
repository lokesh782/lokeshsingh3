
print("Welcome to the Magic Forest")


choice = input("Do you want to go north or south? ").lower()

if choice == "south":
    print("Game Over")
elif choice == "north":
   
    action = input("Do you want to cross the river or follow the path? ").lower()

    if action == "cross the river":
        print("Game Over")
    elif action == "follow the path":
        
        creature = input("Choose between fairy, ogre, or elf: ").lower()

        if creature == "ogre" or creature == "fairy":
            print("Game Over")
        elif creature == "elf":
            print("You win!")
        else:
            print("Invalid choice. Game Over.")
    else:
        print("Invalid action. Game Over.")
else:
    print("Invalid choice. Game Over.")
