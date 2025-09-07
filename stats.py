


# counts the words and returns the amount of words in a text.
def number_of_words(text):
    return len(text.split())


# sorts the item
def sort_on(item):
    return item["num"]

# number of times each character, (including symbols and spaces), appears in the string.
def number_of_char(text):
    words_dict = {}
    for i in text.lower():
         words_dict[i] = words_dict.get(i, 0) + 1
    return words_dict

def sort_function(counts):
    dict_list = []
    for ch, n in counts.items():
        dict_list.append({"char": ch, "num": n})
    dict_list.sort(reverse=True, key=sort_on,)
    return dict_list