# Calculate kilometers per liter

print("This program calculates kilometers per liter")

# Ask input from user
kilometersDriven = input("Enter kilometers driven: ")

# Convert text to float
kilometersDriven = float(kilometersDriven)

# Get liters used from user
litersUsed = input("Enter liters used: ")

# Convert text to float
litersUsed = float(litersUsed)

# Calculate and print the kmpl
kmpl = kilometersDriven / litersUsed
print("Kilometers per liter: ", kmpl)
