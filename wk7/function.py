"""
2 July 2025
Function
"""

# Implement a function that perform simple multiplication

num1 = 3
num2 = 6

result = num1*num2

# print(result)

# Function with no parameter/argument
def simpleMult1():
    print("Function with no parametr/argument")

# Function with parameter/argument and print function
def simpleMult(x, y):
    result = x*y
    # return result
    print(f"Welcome to class {result}")

# Function with a single paramenter/argument and return value
def sumMult(x):
    name = x
    return name

# calling of defined functions
simpleMult1()
simpleMult(23, 89)
print(sumMult("Sam"))
# print(simpleMult())
simpleMult(9,10)

def nameValidation(name):
    if name =="Harira":
        print("Correct")
    else:
        print("Wrong try again")

# nameValidation(input("Please guess a name: "))

# #function using while loop
def scoreCount(num1, num2, count, step):
    while num1>num2:
        num1 = (num1) - step
        count +=1
        print("You are welcome", count)

josh1 = float(input("Enter the first number: "))
josh2 = float(input("Enter the second number 2: "))
josh3 = float(input("Please enter the initial count value: "))
josh4 = float(input("Please enter the step value: "))
scoreCount(josh1, josh2, josh3 ,josh4)

# class work Define a function that receive 4 fruit name from a user, print the fruit name on a list
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
"""

def findFruit(ListFruit):
    for x in ListFruit:
        print(x)

fruits = ["Cherry", "Apple", "Banana"]
findFruit(fruits)
flowers =["Rose", "Habiscus", "Sun flower", "lily"]
findFruit(flowers)

"""
let your function receive fruits list from user, the output your list in a list format as ["bana', 'manago', 'pear']
"""
