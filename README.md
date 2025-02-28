# Password
This repository contains a Python script to generate secure random passwords with a mix of uppercase letters, lowercase letters, digits, and special characters.
Functions Used and Program Flow
Functions:
generate_password(length=12): This function generates a secure random password of the specified length. It:
Defines character pools for uppercase letters, lowercase letters, digits, and special characters.
Ensures that the generated password includes at least one character from each category.
Uses random.choices() to fill the remaining length of the password with a mix of characters.
Randomly shuffles the password to avoid predictable patterns.

Program Flow:
The script starts by defining the generate_password function.
It constructs a list of required characters from each category.
It fills the remaining characters using random.choices().
The password list is shuffled for randomness.
The script then calls generate_password(16) and prints the generated password
