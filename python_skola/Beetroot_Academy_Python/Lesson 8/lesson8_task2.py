def numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ZeroDivisionError:
        return "You can't divide by zero."
    except ValueError:
        return "You need to enter numbers only."
    return a ** 2 / b



print(numbers())