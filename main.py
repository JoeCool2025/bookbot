from stats import book_word_count
from stats import count_book_characters
from stats import sort_character_count

path_to_file = "/home/adin-admin/boot_dev/bookbot/books/frankenstein.txt"
characters_used = count_book_characters(path_to_file)

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count(path_to_file)} total words")
    print("--------- Character Count -------")
    for dictionary in sort_character_count(characters_used):
        if dictionary["name"].isalpha() == True:
            print(f"{dictionary["name"]}: {dictionary["num"]}")
    print("============= END ===============")


main()
