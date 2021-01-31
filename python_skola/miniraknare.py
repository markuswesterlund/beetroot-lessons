def main():
    yeslist = ("y", "yes", "Yes", "YES")
    print('Welcome to Markus Calculator')
    while True:
        try:
            a = float(input("Enter your first number:"))
            b = float(input("Enter your second number:"))
        except ValueError:
            print("Sorry, you need to enter a number")
            continue
        else:
            break

    print("Addition:", a, "+", b, "=", a + b)
    print("Subtraction:", a, "-", b, "=", a - b)
    print("Division:", a, "/", b, "=", a / b)
    print("Multiplication:", a, "*", b, "=", a * b)
    print("Modulus:", a, "%", b, "=", a % b)
    print("Power:", a, "**", b, "=", a ** b)
    print("Floor division:", a, "//", b, "=", a // b)

    restart = input("Do you want to start again? Yes/No")

    if restart in yeslist:
        main()
    else:
        quit()


main()
