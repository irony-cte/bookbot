import sys
from stats import get_num_words
from stats import get_char_count
from stats import get_char_report

#  checks if a file path is provided as a command line argument, closing the program if not
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path_to_file = sys.argv[1]
#  returns the text of a book from a file
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def sort_on(items):
    return items["num"]


def main():
    print("============ BOOKBOT ============")
    #path_to_file = "./books/frankenstein.txt"
    print(f"Analyzing book found at {path_to_file}")
    file_contents = get_book_text(path_to_file)
    num_words = get_num_words(file_contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_report = get_char_report(file_contents)
    char_report.sort(reverse=True, key=sort_on)
    for char_dict in char_report:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

main()