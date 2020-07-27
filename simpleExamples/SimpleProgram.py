# Simple questions to a user

# Enter name
name = input("What is your name? ")
print("Hello " + name + "! ")

# Enter age
age = input("What is your age? ")
print("That's great, " + name + "!  ")

# Ask for temperature outside
temperature = float(input("What is the temperature outside? "))

if temperature > 25:
    print("Wear shorts! ")
    
else:
    print("Wear long pants! ")


print("Enjoy your day " + name + "! ")
