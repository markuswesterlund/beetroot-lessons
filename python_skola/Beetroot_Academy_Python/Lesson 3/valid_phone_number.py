phone_number = input("Enter your phone number here:")

if phone_number.isdigit() and len(phone_number) == 10:
    print("Valid number")
else:
    print("Invalid")
