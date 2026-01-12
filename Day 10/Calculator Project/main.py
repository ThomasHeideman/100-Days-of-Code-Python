def calculator():
    """
    Starts the main calculator program.
    - Manages the program's lifecycle, including recursion for new sessions.
    - Handles user input for numbers and operations.
    - Maintains state by allowing continuation with previous results.
    :return: None (This function runs the application loop).
     """
    from art import logo
    print(logo)

    def add(a, b):
        """
         Calculates the sum of two numbers
        :param a: number, int or float
        :param b: number, int or float
        :return: addition of a and b
        """
        return a + b
    def subtract(a, b):
        """
         Calculates the subtraction of two numbers
        :param a: number, int or float
        :param b: number, int or float
        :return: difference of a and b
        """
        return a - b

    def multiply(a, b):
        """
         Calculates the multiplication of two numbers
        :param a: number, int or float
        :param b: number, int or float
        :return: product of a and b
        """
        return a * b
    def divide(a, b):
        """
         Calculates the division of two numbers
        :param a: number, int or float
        :param b: number, int or float
        :return: quotient of a and b
        """
        return a / b
    methods = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    should_continue = True

    def calculate(num_1, num_2, calc_method):
        """
        Performs the calculation by looking up the operator in the dictionary.
        :param num_1: The first number for the calculation (int or float).
        :param num_2: The second number for the calculation (int or float).
        :param calc_method: The operation symbol (+, -, *, /) as a string.
        :return: The result of the operation as a float.``
        """
        result = float(methods[calc_method](num_1,num_2))
        return result

    n1 = float(input("Enter first number: "))

    while should_continue:
        for method in methods:
            print(f"[ {method} ]")
        operation = input("Enter operation: ")
        n2 = float(input("Enter second number: "))
        output = calculate(n1, n2, operation)
        print(f"{n1} {operation} {n2} ={output}")
        continue_calc = input(f"do you want to continue with {output} type 'y', if you want to start with new calculation type 'n': ")
        if continue_calc == 'y':
            n1 = output
        elif continue_calc == 'n':
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()



