#  returns the number of words in a file
def get_num_words(file_contents):
        words = file_contents.split()
        num_words = len(words)
        return num_words

#  returns the number of times each character appears in a file
def get_char_count(file_contents):
    char_count = {}
    for char in file_contents:
        lcase = char.lower()
        if lcase in char_count:
            char_count[lcase] += 1
        else:
            char_count[lcase] = 1
    return char_count



def get_char_report(file_contents):
    char_count = get_char_count(file_contents)
    char_report = []
    for char, count in char_count.items():
        char_report.append({"char": char, "num": count})
    return char_report