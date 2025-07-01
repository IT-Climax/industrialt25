"""
This session we will deal with python inbuilt library
Internal
math, random, os, json, datetime, system, time, string, statistics, re

"""


import math, random, os, json, sys, time, string, statistics, re
from datetime import datetime


number = 16
sqrt_value = math.sqrt(number)
print(f"The square root of {number} is {sqrt_value}")

# find Cosine with degree
# angle_radians = math.pi / 3 
# cos_value = math.cos(angle_radians)
# print(f"The cosine of 60 degrees is {cos_value}")

# # Random numbers
# rand_int = random.randint(1, 10)
# print(f"Random integer between 1 and 10: {rand_int}")

# #  Suffle human name
# names = ["Alice", "Bob", "Charlie", "Diana"]
# random.shuffle(names)
# print("Shuffled names:", names)

# # get current os directory
# cwd = os.getcwd()
# print(f"Current working directory: {cwd}")

# list files in the current directory
entries = os.listdir('.')
print("Files and directories:", entries)

# # conver dictionary to json file
# person = {"name": "John", "age": 30, "city": "New York"}
# person_json = json.dumps(person)
# print("JSON string:", person_json)

# # revert json to dictionary
# json_str = '{"name": "Anna", "age": 25, "city": "London"}'
# person_dict = json.loads(json_str)
# print("Parsed dictionary:", person_dict)


# print the curent time
# now = datetime.now()
# print("Current date and time:", now)

# #  computation on date
# date1 = datetime(2025, 6, 30)
# date2 = datetime(2024, 6, 30)
# difference = date1 - date2
# print(f"Difference between dates: {difference.days} days")

# # # print python version
# # print("Python version:", sys.version)

# # calculate time taken
# start = time.time()
# for i in range(1000000):
#     pass
# end = time.time()
# print(f"Time taken: {end - start} seconds")

# # search for key word
# print("All lowercase letters:", string.ascii_lowercase)
# print("All uppercase letters:", string.ascii_uppercase)


# # remove punctuation marks
# text = "Hello, world! How's everything?"
# no_punct = ''.join(cha for cha in text if cha not in string.punctuation)
# print("Text without punctuation:", no_punct)

# # Statistics
# # mean
# data = [10, 20, 30, 40, 50]
# mean_value = statistics.mean(data)
# print(f"Mean value: {mean_value}")

# # median
# data = [1, 3, 3, 6, 7, 8, 9]
# median_value = statistics.median(data)
# print(f"Median value: {median_value}")


# # regular expression with search
# text = "An apple a day keeps the doctor away."
# words_starting_with_a = re.findall(r'\ba\w*', text, re.IGNORECASE)
# print("Words starting with 'a':", words_starting_with_a)

# # Masking numbers
# text = "My phone number is 123-456-7890."
# masked_text = re.sub(r'\d', '#', text)
# print("Masked text:", masked_text)

# text = """++++
# Contact us at 123-456-7890 or (987) 654-3210.
# Emergency number: 911.
# Alternate: 555.123.4567
# """

# # egex pattern to match phone numbers in common formats:
#  # Replace digits with '#', keep non-digits
# phone_pattern = re.compile(r'''
#     # Phone number patterns:
#     (                   # Start group for the whole phone number
#         (?:\(\d{3}\))   # Area code with parentheses e.g. (234)
#         [\s.-]?         # Optional separator (space, dot, or dash)
#         \d{3}           # First 3 digits
#         [\s.-]?         # Optional separator
#         \d{4}           # Last 4 digits
#     )
#     |
#     (                   # OR
#         \d{3}           # 3 digits
#         [\s.-]?         # Optional separator
#         \d{3}           # 3 digits
#         [\s.-]?         # Optional separator
#         \d{4}           # 4 digits
#     )
# ''', re.VERBOSE)

# def mask_phone(match):
#     phone = match.group()
#     return re.sub(r'\d', '#', phone)

# masked_text = phone_pattern.sub(mask_phone, text)
# print(masked_text)

# """
# Class work
# 1. Write a Python function mask_digits(text) that replaces all digits in the input string text with the character

# 2.Input: "Call 123-456-7890 or 987-654-3210"
# Output: "Call ###-###-#### or ###-###-####"
# """

"""
External
numpy, panda, matplotlib, request, django, flask, skit-learn, pygame
"""

#  Numpy


# Panda


# # Matplotlib
# import matplotlib as plt

# x = [1,2,3,4,5,6.7,8,9,10]
# y = [5,2,4,4,8,7,4,8,10,9]
# plt.plot(x,y)
# plt.xlabel('Time (s)')
# plt.ylabel('Temperature (degC)')
# # plt.show()