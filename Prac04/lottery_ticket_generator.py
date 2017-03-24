"""
Program generates 6 random lottery picks as follows:
- asks user for the number of "quick picks";
- then program generates a line of six random number between 1 - 45;
- each line has no repeated numbers;
- lines are displayed in ascending order
"""

import random

num_quick_pics = int(input("How many quick pics?"))
for i in range(num_quick_pics):
    quick_pics = []
    for j in range(6):
        num = random.randint(1, 45)
        while num in quick_pics:
            num = random.randint(1, 45)
        quick_pics.append(num)
    quick_pics.sort()
    print(quick_pics)
