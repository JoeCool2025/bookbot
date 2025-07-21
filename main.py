from stats import book_word_count
from stats import count_book_characters

path_to_file = "/home/adin-admin/boot_dev/bookbot/books/frankenstein.txt"
characters_used = count_book_characters(path_to_file)

def main():
    text = book_word_count(path_to_file)
    print(f"{text} words found in the document")
    print(characters_used)


main()
