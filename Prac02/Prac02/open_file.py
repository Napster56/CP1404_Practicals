# Program opens a file; gets name from the user; and then saves their name to the file.
input_file = open("name.txt", "w")
user_name = input("Enter your name: ")
print(user_name, file=input_file)
input_file.close()





