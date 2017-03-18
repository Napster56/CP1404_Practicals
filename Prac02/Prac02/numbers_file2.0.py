input_file = open("numbers.txt", "r")
total = 0
for line in input_file:
    num = int(line)
print(total)
input_file.close()
