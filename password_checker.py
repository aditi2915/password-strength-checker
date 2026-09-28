password = input("Enter a password to check: ")

length_ok = len(password) >= 8
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

score = 0

if length_ok:
    score += 1

if has_uppercase:
    score += 1

if has_lowercase:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

print("\nPassword Security Check")
print("-----------------------")

print("Length requirement:", length_ok)
print("Uppercase letter:", has_uppercase)
print("Lowercase letter:", has_lowercase)
print("Number:", has_digit)
print("Special character:", has_special)

print("\nScore:", score, "/ 5")

if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Moderate")
else:
    print("Strength: Strong")
