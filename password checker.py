import re

def check_password_complexity(password):
    
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    
    errors = {
        "Minimum 8 characters": not length_error,
        "Contains digit": not digit_error,
        "Contains uppercase": not uppercase_error,
        "Contains lowercase": not lowercase_error,
        "Contains special character": not symbol_error
    }

    
    is_strong = all(errors.values())

    print("\nPassword Check Results:")
    for rule, passed in errors.items():
        print(f"✔️ {rule}" if passed else f"❌ {rule}")

    if is_strong:
        print("\n✅ Password is STRONG.")
    else:
        print("\n⚠️ Password is WEAK. Please meet all the criteria.")


password = input("Enter your password: ")
check_password_complexity(password)
