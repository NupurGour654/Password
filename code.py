import random
import string
import pyperclip
import logging
logging.basicConfig(level=logging.INFO)



def generate_password(length=12,use_symbols=True):
    """Generate a secure random password with uppercase, lowercase, digits, and special characters."""
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation if use_symbols else ''

    
    all_chars = uppercase + lowercase + digits + special_chars
    password = [
        random.choice(uppercase),
        random.choice(lowercase)
        random.choice(digits),
        random.choice(special_chars)
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
