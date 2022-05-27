# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string


def read_file_content(filename):
    # Open and read file 
    with open(filename) as f:
        content = f.read()
    
    return content


def count_words():
    text = read_file_content("./story.txt")
    # Remove punctuations from the texts
    words = text.translate(str.maketrans('', '', string.punctuation))
    # change all letters to lower case and split words into a list
    words_list = words.lower().split()
    words_dictionary = {}
    # Count words and add them to a dictionary
    for item in words_list:
        if item in words_dictionary:
            words_dictionary[item] += 1
        else:
            words_dictionary[item] = 1   

    return words_dictionary

word_count = count_words()
print(word_count)