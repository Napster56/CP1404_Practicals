"""
Program asks user to input numbers, which are stored in a list.
Then uses the list to explore various list methods.
"""

numbers = []
for i in range(5):
    num = int(input("Enter 5 numbers for your list: "))
    numbers.append(num)

print("The first number is {}\nThe last number is {}\nThe smallest number is {}\
     \nThe largest number is {}\nThe average of the numbers is {}".format(numbers[0], numbers[4], min(numbers),
     max(numbers), sum(numbers) / len(numbers)))
