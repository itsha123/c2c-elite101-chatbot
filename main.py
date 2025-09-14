name = input("What is your name? ")
age = int(input("What is your age? "))
print(f"Welcome {name}! How can I help you? ")
while True:
    menuOption = int(input("""
    1. Placeholder
    2. Placeholder
    3. Placeholder
    4. Exit
    """))
    if menuOption == 4:
        print("Goodbye!")
        break