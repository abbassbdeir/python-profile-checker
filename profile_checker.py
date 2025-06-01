def get_user_info():
    name = input("Enter your Name: ").strip()
    age = int(input("Enter your Age: ").strip())
    gpa = float(input("Enter your GPA (0-5): ").strip())
    field = input("Enter your Field of Interest: ").strip()
    graduated = input("Have you graduated? (yes/no): ").strip().lower()
    return {
        "name": name,
        "age": age,
        "gpa": gpa,
        "field": field,
        "graduated": graduated == "yes"
    }


def print_info(user):
    print("\n--- User Information ---")
    print(f"Name            : {user['name']}")
    print(f"Age             : {user['age']}")
    print(f"GPA             : {user['gpa']}")
    print(f"Field of Interest: {user['field']}")
    print(f"Graduated       : {'Yes' if user['graduated'] else 'No'}")
    print("------------------------\n")


def evaluate_eligibility(user):
    if user['age'] < 25 and user['gpa'] >= 3.5 and user['graduated']:
        print("Congratulations! You are eligible for a scholarship.")
    elif user['age'] < 30 and user['gpa'] >= 2.5:
        print("Good news! You are eligible for an internship.")
    else:
        print("Thank you for your interest. Please consider applying again later.")


def main():
    user = get_user_info()
    print_info(user)
    evaluate_eligibility(user)


if __name__ == "__main__":
    main()
