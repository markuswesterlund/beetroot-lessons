def main():

    yeslist = ("y", "yes", "Yes", "YES")
    print('Welcome to Markus Calculator')
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))

    print('Addition: ', str(a), '+', str(b), '=', a + b)
    print('Subtraction: ', str(a), '-', str(b), '=', a - b)
    print('Division: ', str(a), '/', str(b), '=', a / b)
    print('Multiplication: ', str(a), '*', str(b), '=', a * b)
    print('Modulus: ', str(a), '%', str(b), '=', a % b)
    print('Power: ', str(a), '**', str(b), '=', a ** b)
    print('Floor division: ',str(a), '//', str(b), '=', a // b)

    restart = input("Do you want to start again? Yes/No ")

    if restart in yeslist:
        main()
    else:
        exit()
main()
