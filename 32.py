
weather = input("Enter the current weather (sunny/rainy): ").lower()
if weather == "sunny":
    print("It's a great day! You can go for hiking or have a picnic.")
elif weather == "rainy":
    rain_gear = input("Do you have a raincoat or umbrella? (yes/no): ").lower()
    
    if rain_gear == "yes":
        print("You can go to a nearby mall or museum!")
    else:
        print("It's better to stay home and watch movies.")
else:
    print("Invalid weather input. Please enter 'sunny' or 'rainy'.")
