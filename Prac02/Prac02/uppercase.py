import random

import string

lower_char = string.ascii_lowercase
upper_char = string.ascii_uppercase
special_char = string.punctuation
password = []
upper = 2
#generate_upper(password, upper):
'''for i in range(upper):
    random_upper = random.choice(string.ascii_uppercase)
    password.append(random_upper)
print(password)'''

for i in range(6               ):

        password += random.choice(upper_char)
        password += random.choice(lower_char)
        password += random.choice(special_char)
        i += 1
        print(password)