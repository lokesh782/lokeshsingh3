
weight = float(input("Enter the weight of the package (in kg): "))
urgent = input("Is the delivery urgent? (yes/no): ").lower()
if weight < 5:
    cost = 5
elif 5 <= weight <= 20:
    cost = 10
else:
    cost = 20
if urgent == "yes":
    cost += 5
print(f"The delivery cost is: ${cost}")
