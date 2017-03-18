try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
# ValueError occurs when the value of either the numerator or denominator is not an integer.
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# ZeroDivisionError occurs when denominator equals zero.
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
