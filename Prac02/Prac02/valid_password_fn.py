password = "Napster1956"
MIN_LENGTH = 2
MAX_LENGTH = 6
if MIN_LENGTH < len(password) < MAX_LENGTH:
    print("False")
count_lower = 0
count_upper = 0
count_digit = 0
count_special = 0
for char in password:
    if char.islower():
        count_lower += 1
    elif char.isupper():
        count_upper += 1
    elif char.isdigit():
        count_digit += 1
    elif char.isspecial:
        count_special += 1
print(count_lower)
print(count_upper)
print(count_digit)
print(count_lower)