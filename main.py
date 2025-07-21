from stats import book_word_count
from stats import count_book_characters
from stats import sort_character_count
import sys

path_to_file = ""

try:
    path_to_file = sys.argv[1]
except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    characters_used = count_book_characters(path_to_file)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count(path_to_file)} total words")
    print("--------- Character Count -------")
    for dictionary in sort_character_count(characters_used):
        if dictionary["name"].isalpha() == True:
            print(f"{dictionary["name"]}: {dictionary["num"]}")
    print("============= END ===============")


main()
