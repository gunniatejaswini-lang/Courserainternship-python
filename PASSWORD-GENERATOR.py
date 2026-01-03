import random
import string

def generate_password(length, upper, lower, digits, symbols):
    characters = ""
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if characters == "":
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if len(password) >= 12: score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

print("PASSWORD GENERATOR SYSTEM")
print("--------------------------")

length = int(input("Enter password length: "))

upper = input("Include uppercase letters (y/n): ").lower() == 'y'
lower = input("Include lowercase letters (y/n): ").lower() == 'y'
digits = input("Include numbers (y/n): ").lower() == 'y'
symbols = input("Include symbols (y/n): ").lower() == 'y'

password = generate_password(length, upper, lower, digits, symbols)

if password:
    print("\nGenerated Password:", password)
    print("Password Strength:", check_strength(password))
else:
    print("Error: No character set selected")
