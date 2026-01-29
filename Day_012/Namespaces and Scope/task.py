# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


def is_prime(num):

    if num < 2:
        return False
    for number in range(2, num):
        if num % number == 0:
            return False
    return True


is_prime(9)