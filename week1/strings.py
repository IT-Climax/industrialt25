"""
String Manipulation
MODULE 2: STRING MANIPULATION
"""

school = "Madibo Adama University Yola"
school2 = "American Univerity of Nigeria"
text = """
Welcome to Mentors Innovation Hub Nigeria. 
We are glad you are here with us today. 
Your presence is most value and we will give you the best any client can offer
"""

# greeting = "How are you!"
# question = "what would you have me for you today!"

# # Count
# print("Character count:", len(school))
# print("Data type", type(school2))


# # Lesson 1: Understanding Strings
# name = "Bosun"
# message = '''Welcome to Python!'''
# print(type(name))


# # # Lesson 2: String Operations
# first_name = "Bosun"
# last_name = "Adeniyi"

# full_name = first_name + ", " + last_name
# fullname = "Bosun, Adeniyi"
# # print("Hello!", full_name)
# # print(f'Hello! {first_name}, {last_name}')

# repeat = "Hi!" * 100
# print(repeat)

# sliced = full_name[0:5]
# print(sliced)

# # class work: print out firstname and Initial of the the surname e.g "A. Bosun"

# slicedInit = full_name[7]
# print(f"{slicedInit}. {first_name}")

# # Lesson 3: Escape Characters & Formatting
# item = "Pen"
# price = 50
# receipt = f"You bought a {item}\nTotal: \tN{price}"
# print(receipt)

# STRING METHODS

# # Lesson 4: Case Methods
# text = "python is Fun"
# print(text.title())
# print(text.upper())
# print(text.swapcase())

# # Lesson 5: Search and Check Methods
# sentence = "Hello, welcome to Python class."
# print(sentence.find("Python"))
# print(sentence.startswith("Hello"))
# print("12345".isdigit())

# print("Check full name",full_name.endswith("Hello"))
# print("Check full name",full_name.startswith("Bosun"))



# # Lesson 6: Split and Join
# words = sentence.split()
# print(words)
# joined = "_".join(words)
# print(joined)

# # Lesson 7: Strip and Clean Text
# dirty = "   Hello, Python!   "
# clean = dirty.strip()
# print(clean)
 
 #IF, If-else(elif), For, While, 

# STRING LOGIC

# Lesson 8: String Loops & Conditionals
vowels = "aeiou"
word = "Hello"
vowel_count = 0
for letter in word.lower():
    if letter in vowels:
        vowel_count += 1
print(f"Vowels: {vowel_count}")

# a = 33
# b = 22
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#    print("b is less than a Joshua")

# write a code to do binary search.

# Palindrome Checker
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("level"))

# Lesson 9: Mini Text Game - Word Scramble
def scramble(word):
    return ''.join(sorted(word))

print("Scrambled: ", scramble("python"))

# ADVANCED STRING TECHNIQUES

# Lesson 10: Regular Expressions
import re
email = "us.23_er@_example.com"
pattern = r"[\w.-]+@[\w.-]+\.\w+"
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
# # Lesson 11: Advanced Formatting
name = "Bosun"
score = 89.456
print(f"Name: {name:>2} | Score: {score:.2f}")

# Lesson 12: Encoding/Decoding
text = "Encode this!"
encoded = text.encode("utf-8")
encoded2 = text.encode("utf-32")
decoded = encoded.decode("utf-8")
decoded2 = encoded2.decode("utf-32")
print(decoded)
print(f"New encoding key: {decoded2}")

# PRO-LEVEL STRING USE CASES

# # Lesson 13: Text Cleaning for NLP
# import string
# raw_text = "Hello!! This, is some TEXT!!!"
# cleaned = raw_text.lower()
# cleaned = cleaned.translate(str.maketrans('', '', string.punctuation))
# print(cleaned)

# # Lesson 14: Data Parsing from CSV-style text
# data = "John,25,Developer"
# name, age, role = data.split(",")
# print(f"Name: {name}, Age: {age}, Role: {role}")

# # Lesson 15: Capstone Project - Simple Text Analyzer
# def analyze(text):
#     words = text.split()
#     return {
#         "word_count": len(words),
#         "longest_word": max(words, key=len),
#         "most_common": max(set(words), key=words.count)
#     }

# sample = "hello world hello students in python world"
# result = analyze(sample)
# print(result)
