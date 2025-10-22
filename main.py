# This project was made with the assistance of Github Copilot (autocompletions and next edit suggestions)

name = input("What is your name? ")
print(f"Welcome to the DMV Services Chatbot, {name}!")
while True:
    while True:
        registerVehicle = input("Would you like to register a vehicle? (yes/no) ")
        if registerVehicle.lower() == "no":
            print("Sorry, this chatbot only supports vehicle registration. Have a nice day!")
            exit()
        elif registerVehicle.lower() == "yes":
            print("Great! Let's get started with the vehicle registration.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    vehicleIdentificationNumber = input("Please enter your Vehicle Identification Number (VIN): ")
    
    carMake = input("Please enter your car's make: ")
    carModel = input("Please enter your car's model: ")
    carYear = input("Please enter your car's year: ")

    ownerSSN = input("Please enter your Social Security Number (SSN): ")
    ownerDOB = input("Please enter your date of birth (mm/dd/yyyy): ")
    ownerGender = input("Please enter your gender: ")
    ownerAddress = input("Please enter your address: ")
    ownerNumber = input("Please enter your phone number: ")
    ownerEmail = input("Please enter your email address: ")

    print("The cost is $15.00 to register a vehicle.")
    print("You can pay by card.")
    while True:
        isSame = input("Is the cardholder name the same as the owner name? (yes/no) ").lower()
        if (isSame == "yes"):
            cardName = name
            break
        elif (isSame == "no"): 
            cardName = input("Please enter the cardholder's name: ")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    while True:
        isSame = input("Is the billing address the same as the owner address? (yes/no) ").lower()
        if (isSame == "yes"):
            cardAddress = ownerAddress
            break
        elif (isSame == "no"):
            cardAddress = input("Please enter the billing address: ")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    cardNumber = input("Please enter your card number: ")
    cardExpiry = input("Please enter your card's expiration date (mm/yy): ")
    cardCVV = input("Please enter your card's CVV: ")