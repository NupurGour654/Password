import random
import string
import pyperclip
import logging

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = string.punctuation


logging.basicConfig(level=logging.INFO)



def generate_password(length=12,use_symbols=True):
    """Generate a secure random password with character diversity."""
    special_chars = SYMBOLS if use_symbols else ''
    all_chars = UPPERCASE + LOWERCASE + DIGITS + special_chars

    password = [
        random.choice(UPPERCASE),
        random.choice(LOWERCASE),
        random.choice(DIGITS),
        random.choice(special_chars) if use_symbols else random.choice(DIGITS)
    ]

    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

def main():
    
def main():
    """Takes user input, validates, and generates password."""
    try:
        length = int(input("Enter password length (min 8): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if length < 8:
        print("Password too short. Use 8+ characters.")
        return

    use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_symbols)
    print("Generated Password:", password)

    logging.info("Password generated successfully.")

    pyperclip.copy(password)
    print("Password copied to clipboard.")

    # Optional: Strength checker
    if length < 10:
        print("Strength: Weak")
    elif length < 14:
        print("Strength: Moderate")
    else:
        print("Strength: Strong")

if __name__ == "__main__":
    main()
