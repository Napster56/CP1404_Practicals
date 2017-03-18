"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def get_score():
    score = float(input("Enter score: "))
    return score


def main():
        score = get_score()
        if 90 < score <= 100:
            print("Excellent")
        elif 50 < score <= 90:
            print("Passable")
        elif 0 <= score <= 50:
            print("Bad")
        else:
            print("Invalid score")
main()

