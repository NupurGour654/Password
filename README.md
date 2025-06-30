#  Password Generator

This repository contains a Python script to generate secure, customizable passwords. The script ensures a strong mix of uppercase letters, lowercase letters, digits, and special characters — suitable for personal, professional, or development use.

---

##  Features

- Randomized password generation
- Guaranteed inclusion of all character types (uppercase, lowercase, digit, symbol)
- User-defined password length
- Option to include or exclude special characters
- Password strength feedback (Weak, Moderate, Strong)
- Clipboard copy support (`pyperclip`)
- Clean modular design with `main()` and helper function
- Input validation for better user experience

---

##  How It Works

###  Function: `generate_password(length=12, use_symbols=True)`

This function handles the core logic for generating a secure password:
- Defines pools for:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Digits (0–9)
  - Symbols (if enabled)
- Ensures the password contains **at least one** character from each selected category
- Fills the remaining length using `random.choices()` from the full combined pool
- Shuffles the result to remove predictable ordering
- Returns the final password as a string

---

##  Program Flow

1. The script starts by asking the user for the desired password length.
2. It checks for valid input (minimum 8 characters).
3. The user can choose whether to include special characters.
4. The `generate_password()` function is called with these parameters.
5. The password is printed and copied to the clipboard.
6. A password strength indicator is displayed based on length.

---

##  Example Output

```bash
Enter password length (min 8): 14
Include special characters? (y/n): y
Generated Password: A5$vfkL8zQ2@hs
Password copied to clipboard.
Strength: Strong
