name = input("What is your name? ")
print(f"Welcome to the DMV Services Chatbot, {name}!")
while True:
    user_input = input("Would you like to register a vehicle? (yes/no) ")
    if user_input.lower() == "no":
        print("Sorry, this chatbot only supports vehicle registration. Have a nice day!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")