import random
import string

def generate_password(length=12):
    """Generate a secure random password with uppercase, lowercase, digits, and special characters."""
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    
    all_chars = uppercase + lowercase + digits + special_chars
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    password += random.choices(all_chars, k=length - 4)
    

    random.shuffle(password)
    
    return ''.join(password)

print("Generated Password:", generate_password(16))
