''' Name: Naman Gupta
    Date: 5 October'25
    Daily Calorie Tracking Console App '''

print("Hello and welcome to a platformm whcih helps you to calculate your daily calorie intake:- ")

meal_name = []
calorie_intake = []

amount = int(input("No of meals per day? "))
calorie_limit = int(input("What is your daily calorie intake limit? "))

for i in range(amount):
    meal = input("Enter your meal name: ")
    calorie_amount = int(input("Calorie intake in this meal: "))
    meal_name.append(meal)
    calorie_intake.append(calorie_amount)

total = sum(calorie_intake)
average_calories = total / amount

if total == calorie_limit:
    print("Hurray! You just hit the perfect daily calorie intake.")
elif total < calorie_limit:
    print("Yay, You ate in calorie deficit (You can have sweets!)")
else:
    print("Oops, You ate in calorie surplus!")

print("\nmeal_name     calorie_intake")
print("-"*40)
print(f"{'Total:':<15}{total:>10.0f}")
print(f"{'Average:':<15}{average_calories:>10.2f}")