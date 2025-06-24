# Text Cleaner Tool Samuel
# Cleaner
import string

def clean_text(text):
    return text.lower().translate(str.maketrans('', '', string.punctuation)).strip()

sample = "  Hello!! This is a Test.   "
print(clean_text(sample))

# Word List Cleaner
def clean_and_split(text):
    cleaned = text.lower().translate(str.maketrans('', '', string.punctuation)).strip()
    return cleaned.split()

print(clean_and_split(sample))

# # Project 2: Student Grade Formatter
# # Version 1 - Simple Alignment
# students = [
#     ("Alice", 85),
#     ("Bob", 74),
#     ("Cathy", 92)
# ]

# for name, score in students:
#     grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C'
#     print(f"{name:<10} | {score:>3} | Grade: {grade}")

# # Version 2 - With Table Header and Footer
# def format_grades(students):
#     print(f"{'Name':<10} | {'Score':>5} | Grade")
#     print("-" * 30)
#     for name, score in students:
#         grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C'
#         print(f"{name:<10} | {score:>5} | {grade}")

# format_grades([("David", 88), ("Eva", 95), ("Frank", 77)])

# # Project 3: Simple Resume Parser
# # Version 1 - Using Basic Split
# def parse_resume(text):
#     lines = text.split("\n")
#     for line in lines:
#         if "email" in line.lower():
#             print("Email:", line)
#         elif "phone" in line.lower():
#             print("Phone:", line)

# sample_resume = """
# Name: John Doe
# Email: john.doe@example.com
# Phone: 08123456789
# Skills: Python, Data Analysis
# """
# parse_resume(sample_resume)

# # Version 2 - Using Regex
# import re

# def regex_resume_parser(text):
#     email = re.search(r"[\w.-]+@[\w.-]+", text)
#     phone = re.search(r"\d{11}", text)
#     if email:
#         print("Email:", email.group())
#     if phone:
#         print("Phone:", phone.group())

# regex_resume_parser(sample_resume)

# # Project 4: Custom Email Validator
# # Version 1 - Simple Pattern Match
# email = "user@example.com"
# if "@" in email and "." in email.split("@")[1]:
#     print("Valid Email")
# else:
#     print("Invalid Email")

# # Version 2 - Regex Email Validator
# def is_valid_email(email):
#     pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
#     return re.match(pattern, email) is not None

# print(is_valid_email("user@example.com"))
# print(is_valid_email("user@com"))
