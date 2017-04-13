"""
Program asks user for a string containing several words, then counts how many times each word appears in the string.
Text: this is a collection of words of nice words this is a fun thing it is
"""


def create_word_key_list(count_word, word_key_list):
    for key, count in count_word.items():
        word_key_list.append((key, count))
        sorted_list = sorted(word_key_list)
    print(sorted_list)
    return sorted_list


def create_word_list(count_word, sorted_list):
    for key, count in count_word.items():
        sorted_list.append(key)
        longest_word = max(sorted_list)
        print(longest_word)
        return longest_word


def print_list(longest_word, sorted_list):
    for key, word in sorted_list:
        print("{:{}} : {}".format(key, len(longest_word), word))


def main():
    count_word = {}
    word_key_list = []
    word_list = []

    user_string = input("Enter the words for your string: ")
    string_list = user_string.split()
    print(string_list)
    for word in string_list:
        if word in count_word:
            count_word[word] += 1
        else:
            count_word[word] = 1
    print(count_word)
    create_word_key_list(count_word, word_key_list)
    longest_word = create_word_list(count_word, word_list)
    print_list(longest_word, word_key_list)

main()





