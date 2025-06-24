"""
This session we will deal with python built-in
print(), len(), input(), int(), float(), str(), min(), max(), round()
"""

#Example 1
isStr = input("Enter name-string value: ")
isInt = input("Enter Integer value: ")
isFloat = input("Enter Float value: ")
isList = [3, 8, 9, 20]
print(f"My name {isStr}")

#Example 2
ulength = len(isStr)
print(f"The character count of your {isStr} is : " + str(ulength))

number1 = float(isFloat)
number2 = int(isInt)
print(f"Float number: {number1}")
print(f"Integer number: {number2}")

# Maximum 
isMax = max(isList[0:4])
print("Maximum number in the list is : " + str(isMax))

# Minimum
isMin = min(isList[0:4])
print("Minimum number in the list is : " + str(isMin))

# Round decimal places
isRounded = round(number1, 2)
print("Round to 2 decimal place " + str(isRounded))




