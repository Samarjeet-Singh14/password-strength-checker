import re
import secrets
import string

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "admin", "welcome", "letmein"
}


def check_password_strength(password: str) -> tuple[int, list[str]]:
    """Evaluates password strength and returns a score (0 to 5) and feedback messages."""
    feedback = []
    score = 0

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This is an extremely common password.")
        return 0, feedback

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Must be at least 8 characters long (12+ recommended).")

    # Character set checks
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Missing lowercase letters (a-z).")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Missing uppercase letters (A-Z).")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Missing numeric digits (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Missing special symbols (!@#$%^&*...).")

    return min(score, 5), feedback


def generate_secure_password(length: int = 16) -> str:
    """Generates a cryptographically strong randomized password."""
    if length < 8:
        length = 8

    # Ensure at least one character from each core character set
    mandatory = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*-_+=?"),
    ]

    all_chars = string.ascii_letters + string.digits + "!@#$%^&*-_+=?"
    remaining = [secrets.choice(all_chars) for _ in range(length - len(mandatory))]

    password_list = mandatory + remaining

    # Cryptographically secure in-place Fisher-Yates shuffle
    for i in range(len(password_list) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_list[i], password_list[j] = password_list[j], password_list[i]

    return "".join(password_list)


def main():
    ratings = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong",
    }

    print("=" * 45)
    print("   PASSWORD STRENGTH CHECKER & GENERATOR   ")
    print("=" * 45)

    user_pw = input("Enter a password to test (or press Enter to skip): ").strip()

    if user_pw:
        score, feedback = check_password_strength(user_pw)
        print(f"\nRating: {ratings[score]} (Score: {score}/5)")
        if feedback:
            print("Feedback:")
            for note in feedback:
                print(f" • {note}")
    else:
        print("\nNo password entered for testing.")

    # Generate a strong password alternative
    suggested = generate_secure_password(length=16)
    print("\n" + "-" * 45)
    print(f"Generated Secure Password (16 characters):\n-> {suggested}")
    print("-" * 45)


if __name__ == "__main__":
    main()