print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

# todo: work out how much they need to pay based on their size choice
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
       bill +=2
    else:
        bill += 3
else:
    bill=bill
# todo: work out their final bill based on wether they want extra cheese or not.
if extra_cheese == "Y":
    bill +=1
    print(f"Your final bill is: ${bill}.")
else:
    print(f"Your final bill is: ${bill}.")



# # todo: work out how much they need to pay based on their size choice
# if size == "S":
#     bill = 15
#     print(f"A small pizza is {bill:.2f}")
# elif size == "M":
#     bill = 20
#     print(f"A medium pizza is {bill:.2f}")
# else:
#     bill = 25
#     print(f"A large pizza is {bill:.2f}")
# # todo: work out how much to add to their bill based on their pepperoni choice.
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# if pepperoni == "Y":
#     if size == "S":
#        bill +=2
#        print(f"That will be an extra $2.00, your total is now {bill:.2f}")
#     else:
#         bill += 3
#         print(f"That will be an extra $3.00, your total is now {bill:.2f}")
# else:
#     bill=bill
# # todo: work out their final bill based on wether they want extra cheese or not.
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# if extra_cheese == "Y":
#     bill +=1
#     print(f"That will be an extra $1.00, your final bill is {bill:.2f}")
# else:
#     print(f"Your final bill is {bill:.2f}")
