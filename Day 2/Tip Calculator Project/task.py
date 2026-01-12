print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
# per_person =(bill/people)*float(f"1.{tip}")
bill_with_tip=bill*(1 + tip/100)
per_person =(bill/people)*(1 + tip/100)
print(bill_with_tip)
per_person2 =bill_with_tip/people
print(per_person)
print(f"Each person should pay: ${round(per_person2, 2)}")
print(f"Each person should pay: ${per_person:.2f}")



