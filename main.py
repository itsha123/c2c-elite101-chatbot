name = input("What is your name? ")
print(f"Welcome to the DMV Services Chatbot, {name}!")
while True:
    registerVehicle = input("Would you like to register a vehicle? (yes/no) ")
    if registerVehicle.lower() == "no":
        print("Sorry, this chatbot only supports vehicle registration. Have a nice day!")
        break
    elif registerVehicle.lower() == "yes":
        print("Great! Let's get started with the vehicle registration.")
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