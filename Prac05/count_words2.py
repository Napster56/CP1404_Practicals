"""
Program asks user for a string containing several words, then counts how many times each word appears in the string.
Text: this is a collection of words of nice words this is a fun thing it is
"""


# Counts the number of times each word appears in the string.
def build_dictionary(count_word, user_string):
    string_list = user_string.strip().split()   # splits & strips string into words
    for word in string_list:
        if word in count_word:
            count_word[word] += 1
        else:
            count_word[word] = 1
    return count_word


# Print formatted using longest word in list
def print_list(longest_word, sorted_list):
    for key, word in sorted_list:
        print("{:{}} : {}".format(key, len(longest_word), word))


# Asks the user for a string and prints the number of times each word appears in the string.
def main():
    count_word = {}
    user_string = input("Enter the words for your string: ")
    count_word = build_dictionary(count_word, user_string)
    longest_word = max(count_word.keys(), key=len)          # gets the longest word in dictionary
    sorted_list = [(k, v) for k, v in count_word.items()]   # converts the dictionary to a list with list comprehension
    sorted_list.sort()
    print_list(longest_word, sorted_list)

main()
