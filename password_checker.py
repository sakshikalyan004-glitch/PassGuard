import re
import getpass

# Common weak passwords list
COMMON_PASSWORDS = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "letmein"
]

def check_strength(password):
    score = 0
    feedback = []

    # 1. Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password kam se kam 8 characters ka ho.")

    # 2. Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("1 Uppercase letter (A-Z) add karein.")

    # 3. Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("1 Lowercase letter (a-z) add karein.")

    # 4. Digit Check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("1 Number (0-9) add karein.")

    # 5. Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("1 Special Character (!@#$%^&*) add karein.")

    # 6. Common Password Check
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("Ye bahut common password hai. Bilkul use na karein.")

    # Result
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, feedback, score


def main():
    print("====== PassGuard: Password Strength Checker ======")

    password = getpass.getpass("Enter your password: ")

    strength, feedback, score = check_strength(password)

    print("\nPassword Strength:", strength)
    print("Score:", score, "/6")

    if strength != "STRONG":
        print("\nSuggestions to make it stronger:")
        for tip in feedback:
            print("-", tip)
    else:
        print("\nExcellent! Your password is strong.")


if __name__ == "__main__":
    main()