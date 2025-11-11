# Author: Alisha Rhodes
# File Name: gpa_eval.py
# Description: This app takes student names and GPAs as input, then determines if the student
# qualifies for the Dean's List (GPA ≥ 3.5) or the Honor Roll (GPA ≥ 3.25). The program continues
# to process student records until the last name 'ZZZ' ('zzz') is entered. It only takes names containing
# letters and GPA input is allowed between 1.00 and 4.00.

def is_valid_name(name):
    return name.isalpha()

def is_valid_gpa(gpa):
    return 1.00 <= gpa <= 4.00

while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    if last_name.upper() == 'ZZZ':
        print("Exiting the program. Goodbye!")
        break
    if not is_valid_name(last_name):
        print("Invalid last name. Please use letters only.\n")
        continue

    first_name = input("Enter the student's first name: ")
    if not is_valid_name(first_name):
        print("Invalid first name. Please use letters only.\n")
        continue

    try:
        gpa = float(input("Enter the student's GPA (1.00 - 4.00): "))
        if not is_valid_gpa(gpa):
            print("GPA must be between 1.00 and 4.00. Try again.\n")
            continue
    except ValueError:
        print("Invalid GPA. Please enter a numeric value.\n")
        continue

    print(f"\nStudent: {first_name} {last_name}")
    if gpa >= 3.5:
        print("Congratulations! You've made the Dean's List.\n")
    elif gpa >= 3.25:
        print("Great job! You've made the Honor Roll.\n")
    else:
        print("Keep working hard! You can do it.\n")
        
