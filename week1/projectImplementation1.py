# Project 1: Text Cleaner Tool
# Version 1 - Basic Cleaner with User Input
import string

def clean_text(text):
    # Convert text to lowercase and remove punctuation
    return text.lower().translate(str.maketrans('', '', string.punctuation)).strip()

# Get user input
sample = input("Enter a text to clean: ")
other = input("Enter surname")
print("Cleaned text:", clean_text(sample))

# Version 2 - Word List Cleaner
# This version returns the cleaned words as a list

def clean_and_split(text):
    # Clean the text and split into words
    cleaned = text.lower().translate(str.maketrans('', '', string.punctuation)).strip()
    return cleaned.split()

print("List of cleaned words:", clean_and_split(sample))

# Project 2: Student Grade Formatter
# Version 1 - Simple Alignment with User Input
students = []
num_students = int(input("How many students? "))
for _ in range(num_students):
    name = input("Enter student name: ")
    score = int(input(f"Enter score for {name}: "))
    students.append((name, score))

print("\nFormatted Grade Report:")
for name, score in students:
    grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C'
    print(f"{name:<10} | {score:>3} | Grade: {grade}")

# Version 2 - With Table Header and Footer

def format_grades(student_list):
    print(f"{'Name':<10} | {'Score':>5} | Grade")
    print("-" * 30)
    for name, score in student_list:
        grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C'
        print(f"{name:<10} | {score:>5} | {grade}")

print("\nFull Grade Table:")
format_grades(students)

# Project 3: Simple Resume Parser
# Version 1 - Using Basic Split with User Input

def parse_resume(text):
    # Splits resume line by line and searches for email or phone lines
    lines = text.split("\n")
    for line in lines:
        if "email" in line.lower():
            print("Email:", line)
        elif "phone" in line.lower():
            print("Phone:", line)

print("\nPaste your resume text below (press Enter twice to end):")
resume_lines = []
while True:
    line = input()
    if line == "":
        break
    resume_lines.append(line)
sample_resume = "\n".join(resume_lines)
parse_resume(sample_resume)

# Version 2 - Using Regex
import re

def regex_resume_parser(text):
    # Searches for an email and Nigerian phone number pattern
    email = re.search(r"[\w.-]+@[\w.-]+", text)
    phone = re.search(r"\d{11}", text)
    if email:
        print("Email:", email.group())
    if phone:
        print("Phone:", phone.group())

regex_resume_parser(sample_resume)

# Project 4: Custom Email Validator
# Version 1 - Simple Pattern Match with User Input
user_email = input("\nEnter your email address: ")
if "@" in user_email and "." in user_email.split("@")[1]:
    print("Valid Email")
else:
    print("Invalid Email")

# Version 2 - Regex Email Validator with Function
def is_valid_email(email):
    # Validates email format using regular expression
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return re.match(pattern, email) is not None

print("Using regex validator:", "Valid" if is_valid_email(user_email) else "Invalid")
