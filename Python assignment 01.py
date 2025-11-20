# Name:
# Roll No:
# Course: BCA
# Semester: 1st
# Subject: Problem Solving with Python
# Assignment: Unit-1 Mini Project
# Title: Student Profile Console App
# Date:

def welcome():
    print("-" * 56)
    print("{:^56}".format("STUDENT PROFILE SYSTEM"))
    print("-" * 56)
    print("Welcome! This console app collects and displays a student's profile.")
    print()

def collect_student_info():
    # Task 2: Inputs & variables
    name = input("Enter full name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    program = input("Enter program (e.g., BCA): ").strip()
    university = input("Enter university name: ").strip()
    city = input("Enter city: ").strip()

    # Age should be integer; validate simply
    while True:
        age_str = input("Enter age: ").strip()
        try:
            age = int(age_str)
            break
        except ValueError:
            print("Invalid age. Please enter a whole number (e.g., 18).")

    hobby = input("Enter hobby: ").strip()
    return {
        "name": name,
        "roll_no": roll_no,
        "program": program,
        "university": university,
        "city": city,
        "age": age,
        "hobby": hobby
    }

def operators_demo():
    print("\n--- Operators Demonstration ---")
    # Ask for two numbers
    while True:
        a_str = input("Enter first number (integer): ").strip()
        b_str = input("Enter second number (integer): ").strip()
        try:
            a = int(a_str)
            b = int(b_str)
            break
        except ValueError:
            print("Please enter valid integers.")

    print(f"\nYou entered: a = {a}, b = {b}")

    # Arithmetic
    print("\nArithmetic operators:")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    # handle division by zero
    if b != 0:
        print(f"a / b = {a / b}")
        print(f"a // b = {a // b}")
        print(f"a % b = {a % b}")
    else:
        print("a / b, a // b, a % b -> undefined (division by zero)")

    print(f"a ** b = {a ** b}")

    # Assignment operators demonstration (showing effect on a copy)
    x = a
    print("\nAssignment operators (demonstrated on a copy 'x'):")
    print(f"initial x = {x}")
    x += b
    print(f"x += b -> {x}")
    x = a
    x -= b
    print(f"x -= b -> {x}")
    x = a
    x *= b
    print(f"x *= b -> {x}")
    x = a
    if b != 0:
        x //= b
        print(f"x //= b -> {x}")
    else:
        print("x //= b -> skipped (division by zero)")

    # Comparison
    print("\nComparison operators:")
    print(f"a == b -> {a == b}")
    print(f"a != b -> {a != b}")
    print(f"a > b  -> {a > b}")
    print(f"a < b  -> {a < b}")
    print(f"a >= b -> {a >= b}")
    print(f"a <= b -> {a <= b}")

    # Logical
    print("\nLogical operators (using conditions a>0 and b>0):")
    print(f"(a > 0) and (b > 0) -> {(a > 0) and (b > 0)}")
    print(f"(a > 0) or  (b > 0) -> {(a > 0) or (b > 0)}")
    print(f"not (a > 0) -> {not (a > 0)}")

    # Identity
    print("\nIdentity operators (is / is not) on small ints (caution: implementation detail):")
    c = a
    print(f"a is c -> {a is c}")
    print(f"a is not b -> {a is not b}")

    # Membership
    print("\nMembership operators (in / not in) on a sample string 'hello world':")
    sample = "hello world"
    print("'hello' in sample ->", 'hello' in sample)
    print("'xyz' not in sample ->", 'xyz' not in sample)
    print("--- End of Operators Demo ---\n")

def string_operations(info):
    print("--- String Operations & Formatting ---")
    name = info["name"]
    # Demonstrate concatenation and f-strings
    concat = "Name: " + name
    fstr = f"Student {name} from {info['city']}"

    # escape characters
    escaped = "This\tis\ta\ttab-separated\tline\nAnd this is a new line with a quote: \"Keep learning\""

    # string methods: upper, lower, title, strip, replace, count
    methods = {
        "upper": name.upper(),
        "lower": name.lower(),
        "title": name.title(),
        "strip": name.strip(),
        "replace_spaces": name.replace(" ", "_"),
        "count_a/A": name.lower().count("a")
    }

    print(concat)
    print(fstr)
    print("\nEscaped example:")
    print(escaped)
    print("\nString methods:")
    for k, v in methods.items():
        print(f"{k} -> {v}")
    print("--- End of String Operations ---\n")

def print_profile_card(info):
    print("-" * 56)
    print("{:^56}".format("STUDENT PROFILE"))
    print("-" * 56)
    print(f"Name:            {info['name']}")
    print(f"Roll No:         {info['roll_no']}")
    print(f"Course:          {info['program']}")
    print(f"University:      {info['university']}")
    print(f"City:            {info['city']}")
    print(f"Age:             {info['age']}")
    print(f"Hobby:           {info['hobby']}")
    print("-" * 56)
    print("Welcome to Python Programming !")
    print()

def save_profile(info, path="student_profile.txt"):
    content_lines = [
        "----------------------------------------",
        "          STUDENT PROFILE",
        "----------------------------------------",
        f"Name:            {info['name']}",
        f"Roll No:         {info['roll_no']}",
        f"Course:          {info['program']}",
        f"University:      {info['university']}",
        f"City:            {info['city']}",
        f"Age:             {info['age']}",
        f"Hobby:           {info['hobby']}",
        "----------------------------------------",
        "Welcome to Python Programming !"
    ]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(content_lines))
    print(f"Profile saved to {path}")

def main():
    welcome()
    info = collect_student_info()
    operators_demo()
    string_operations(info)
    print_profile_card(info)

    # Bonus task: ask to save
    save = input("Do you want to save your profile? (yes/no): ").strip().lower()
    if save in ("yes", "y"):
        save_profile(info)
    else:
        print("Profile not saved. You can re-run the program to save later.")

if __name__ == "__main__":
    main()
