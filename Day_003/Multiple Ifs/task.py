print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"Child tickets are {bill:.2f}")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are {bill:.2f}")
    else:
        bill = 12
        print(f"Adult tickets are {bill:.2f}")
    wants_photo= input("Do you want a photo taken? Type y for Yes or n for No. ")
    if wants_photo == "y":
        bill += 3
        print(f"Your bill is: ${bill:.2f}")
    else:
        print(f"Your bill is: ${bill:.2f}")
else:
    print("Sorry you have to grow taller before you can ride.")
