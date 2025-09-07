
from stats import number_of_words, number_of_char, sort_function
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]



def get_book_text (path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main ():
    text = get_book_text(book_path)
    total_words = number_of_words(text)
    char_counts = number_of_char(text)
    sorted_dict = sort_function(number_of_char)
    print(f"{num_words} words found in the document")
    print(number_of_char(text))


def main():
    text = get_book_text(book_path)
    total_words = number_of_words(text)
    char_counts = number_of_char(text) 
    sorted_chars = sort_function(char_counts)
    print(f"""============ BOOKBOT ============
    Analyzing book .................
    ----------- Word Count ----------
    Found {total_words} total words
    --------- Character Count -------""")
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print("============= END ===============")



main ()

