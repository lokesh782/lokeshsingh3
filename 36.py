
print("Welcome to the Space Mission")


choice = input("Do you want to go to the moon or to Mars? ").lower()

if choice == "to mars":
    print("Game Over")
elif choice == "to the moon":
    
    action = input("Do you want to land on the surface or stay in orbit? ").lower()

    if action == "land on the surface":
        print("Game Over")
    elif action == "stay in orbit":
        
        object_choice = input("Choose between alien, asteroid, or satellite: ").lower()

        if object_choice == "alien" or object_choice == "asteroid":
            print("Game Over")
        elif object_choice == "satellite":
            print("You win!")
        else:
            print("Invalid choice. Game Over.")
    else:
        print("Invalid action. Game Over.")
else:
    print("Invalid choice. Game Over.")
