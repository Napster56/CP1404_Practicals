"""
Program asks user for a string containing several words, then counts how many times each word appears in the string.
Text: this is a collection of words of nice words this is a fun thing it is
"""

user_string = input("Enter the words for your string: ")
string_list = user_string.split()

count_word = {}

for word in string_list:
    if word in count_word:
        count_word[word] += 1
    else:
        count_word[word] = 1

word_key_list = []

for key, count in count_word.items():
    word_key_list.append((key, count))
word_key_list.sort()
print(word_key_list)

word_list = []

for key, count in count_word .items():
    word_list.append(key)
print(word_list)
longest_word = max(word_list)  #TODO correct this!!!!!

for key, word in word_key_list:
    print("{:{}} : {}".format(key, len(longest_word), word))
