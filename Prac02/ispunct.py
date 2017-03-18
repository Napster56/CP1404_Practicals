password = "&^%$#"
for char in password:
    if char.ispunct():
        count_special += 1
print(count_special)