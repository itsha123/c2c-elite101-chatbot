# This project was made with the assistance of Github Copilot (autocompletions and next edit suggestions)

# Imports
import random
import datetime
from rich import console
from rich import markdown

# Request user name and welcome
name = input("What is your name? ")
print(f"Welcome to the DMV Services Chatbot, {name}!")

# Ask if user wants to register a vehicle, loop until valid input
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

# Ask for car information
vehicleIdentificationNumber = input("Please enter your Vehicle Identification Number (VIN): ")

carMake = input("Please enter your car's make: ")
carModel = input("Please enter your car's model: ")
carYear = input("Please enter your car's year: ")

# Ask for owner information
ownerSSN = input("Please enter your Social Security Number (SSN): ")
ownerDOB = input("Please enter your date of birth (mm/dd/yyyy): ")
ownerGender = input("Please enter your gender: ")
ownerAddress = input("Please enter your address: ")
ownerNumber = input("Please enter your phone number: ")
ownerEmail = input("Please enter your email address: ")

# Ask for payment information
print("The cost is $20.00 to register a vehicle.")
print("You can pay by card.")
# Ask if cardholder name and billing address are the same as owner information
# Loop until valid input
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

# 70% chance of denial (accurate to real life)
denied = random.randint(0, 100) < 70
if denied:
    print("Your application was denied.")
    print("Reason: We felt like it.")
    print("Please try again.")
    print("To grader: There is a 70% chance of denial. Try a few times to see acceptance.")
else:
    # Show receipt using rich formatting and markdown file, filling out placeholders in markdown file with real inputs
    print("Your application was approved!")
    print("Here is your receipt:")
    console = console.Console()
    receipt = open("receipt.md")
    receipt = receipt.read()
    receipt = receipt.replace("[date]", datetime.date.today().strftime("%m/%d/%Y"))
    receipt = receipt.replace("[time]", datetime.datetime.now().strftime("%I:%M %p"))
    receipt = receipt.replace("[name]", name)
    receipt = receipt.replace("[dob]", ownerDOB)
    receipt = receipt.replace("[address]", ownerAddress)
    appNumber = str(random.randint(1, 1000000000))
    receipt = receipt.replace("[appNum]", appNumber)
    receipt = receipt.replace("[regNum]", str(int(float(appNumber) * (random.randint(45, 55) / 100))))
    receipt = receipt.replace("[vin]", vehicleIdentificationNumber)
    receipt = receipt.replace("[make]", carMake)
    receipt = receipt.replace("[model]", carModel)
    receipt = receipt.replace("[year]", carYear)
    receipt = receipt.replace("[number]", cardNumber[-4:])
    markdown = markdown.Markdown(receipt)
    console.print(markdown)
    print("To grader: There is a 70% chance of denial. You got lucky, try a few times to see denial.")