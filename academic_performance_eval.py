# Author: Alisha Rhodes
# Project: Academic Performance Evaluation Tool
# Description:
# Validates student records, enforces GPA rules, and classifies students
# into performance tiers (Dean's List, Honor Roll, Standard Standing).

def is_valid_name(name: str) -> bool:
    return name.isalpha()

def is_valid_gpa(gpa: float) -> bool:
    return 1.00 <= gpa <= 4.00

def classify_gpa(gpa: float) -> str:
    if gpa >= 3.5:
        return "Dean's List"
    elif gpa >= 3.25:
        return "Honor Roll"
    return "Standard Standing"

def get_student_record():
    last_name = input("Enter last name (or 'ZZZ' to quit): ").strip()
    if last_name.upper() == "ZZZ":
        return None

    if not is_valid_name(last_name):
        print("Invalid last name. Letters only.\n")
        return "retry"

    first_name = input("Enter first name: ").strip()
    if not is_valid_name(first_name):
        print("Invalid first name. Letters only.\n")
        return "retry"

    try:
        gpa = float(input("Enter GPA (1.00 - 4.00): "))
        if not is_valid_gpa(gpa):
            print("GPA must be between 1.00 and 4.00.\n")
            return "retry"
    except ValueError:
        print("Invalid GPA. Numeric values only.\n")
        return "retry"

    return first_name, last_name, gpa

def main():
    print("Academic Performance Evaluation Tool\n")

    while True:
        record = get_student_record()

        if record is None:
            print("Exiting program. Goodbye!")
            break
        if record == "retry":
            continue

        first, last, gpa = record
        standing = classify_gpa(gpa)

        print(f"\nStudent: {first} {last}")
        print(f"Academic Standing: {standing}\n")

if __name__ == "__main__":
    main()
