"""
This session we will deal with python built-in
print(), len(), input(), int(), float(), str(), min(), max(), round()
"""

#Example 1
isStr = input("Enter name-string value: ")
isInt = input("Enter Integer value: ")
isFloat = input("Enter Float value: ")
isList = [3, 8, 9, 20]
data = [1.6, 3.4, 5.5, 9.4]
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

# ort() - sorts the list in ascending order
data.sort()
print("Sorted:", data)

# copy() - creates a shallow copy of the list
copied_data = data.copy()
print("Copied:", copied_data)

# count() - counts how many times a value appears in the list
print("Count of 3.4:", data.count(3.4))

# insert() - inserts an item at a specific position
data.insert(2, 7.1)  # Insert 7.1 at index 2
print("After insert:", data)

# remove() - removes the first occurrence of a value
data.remove(3.4)
print("After remove 3.4:", data)

# clear() - removes all elements from the list
data.clear()
print("After clear:", data)

# Start with a fresh list
data = [1.6, 3.4, 5.5, 9.4]

# reverse() - reverses the list in-place
data.reverse()
print("Reversed:", data)

# pop() - removes and returns the last item (or item at index)
last_item = data.pop()
print("Popped last item:", last_item)
print("After pop:", data)

# extend() - adds elements from another list to the end
data.extend([7.7, 8.8])
print("After extend:", data)



"""
Class work
print(" ".join(["He"] * 3))
"""


