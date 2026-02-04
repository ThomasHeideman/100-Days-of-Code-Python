# region Unlimited positional arguments - *args
def add(*args):
    sum_n = 0
    for n in args:
        sum_n += n
    return sum_n

# print(add(3, 4, 6))

# endregion

# region Unlimited keyword arguments - **args
def calculate(n, **args):
    print(args)
    # for key, value in args.items():
    #     print(key)
    #     print(value)
    n += args["add"]
    n *= args["multiply"]

    print(n)
calculate(2, add=3, multiply=3)

class Car:
    def __init__(self, **args):
        self.make = args.get("make")
        self.model = args.get("model")
        self.colour = args.get("colour")
        self.seats = args.get("seats")

my_car = Car(make="Peugeot", colour="red")
print(my_car.make)
print(my_car.model)

# endregion