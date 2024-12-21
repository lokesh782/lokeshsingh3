
print("Welcome to Treasure Land")

direction = input("Do you want to go left or right? ").lower()

if direction == "right":
    print("Game Over")
elif direction == "left":
    
    action = input("Do you want to swim or wait? ").lower()
    
    if action == "swim":
        print("Game Over")
    elif action == "wait":
        color = input("Choose a color: red, blue, or yellow? ").lower()
        
        if color == "blue" or color == "red":
            print("Game Over")
        elif color == "yellow":
            print("You win!")
        else:
            print("Invalid color choice. Game Over.")
    else:
        print("Invalid action. Game Over.")
else:
    print("Invalid direction. Game Over.")
