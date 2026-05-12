print("Welcome to Nunnah's Boutique")


user_name = input("Enter your User Name: ")

if len(user_name) < 10:
    print('Invalid User Name')
    is_std_username = False
elif len(user_name)>=10:
    print("Successfully logged")
    is_std_username = True
else:
    print("Processed to payments")
    is_std_username = False

print("Thank you for visiting our store")

print('\n1. Go to bankapp\n')
print('2. Enter card number')

choice = input("Enter your choice (1 or 2): ")

if choice == "1" and is_std_username:
    print("Connecting to your BankApp ...")
elif choice == "2" and is_std_username:
    card_number = input("Enter your card number: ")  # Collect card number here
    if len(card_number) == 16 and card_number.isdigit():
        print("Card accepted! Processing payment...")
        print("Payment successful!")
    else:
        print("Invalid card number, please try again")
elif choice == "1" or choice == "2":
    print("Please log in first")
else:
    print("Wrong choice, Try again")




