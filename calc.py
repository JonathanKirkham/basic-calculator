def main():

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        try:
            return a / 0
        except ZeroDivisionError as err2:
            return err2

    global op
    global num1
    global num2

    try:
        num1 = float(input("Number: "))
        op = input("[+ - * /]: ")
        num2 = float(input("Number: "))
    except ZeroDivisionError as err:
        print(err)
    except ValueError as err1:
        print(err1)
        print("Please try again")
        main()

    if op == "+":
        r = add(num1, num2)
        print(num1, "+", num2, "=", r)
    elif op == "-":
        r = subtract(num1, num2)
        print(num1, "-", num2, "=", r)
    elif op == "*":
        r = multiply(num1, num2)
        print(num1, "x", num2, "=", r)
    elif op == "/":
        r = divide(num1, num2)
        print(num1, "/", num2, "=", r)
    elif op == "q":
        exit()
    elif op == "r":
        main()
    else:
        print("Error: Invalid Input")

    q = str(input("Would you like to quit the program? [y/n]: "))
    if q == "y":
        exit()
    elif q == "n":
        main()
    else:
        print("Error: Invalid Input")


main()



