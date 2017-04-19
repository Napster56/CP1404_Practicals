"""
Program takes two parallel lists as input parameters and returns a dictionary,
where keys are from the first list and the values are from the second.
"""

names = ["Jack", "Jill", "Harry"]
dobs = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

new_dict = dict(zip(names, dobs))
print(new_dict)
