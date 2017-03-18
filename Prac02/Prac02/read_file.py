# Program that opens file “name.txt” and reads the name (as above) then prints the name.
output_file = open("name.txt", "r")
user_name = output_file.read().strip()
print("Your name is", user_name)
output_file.close()


