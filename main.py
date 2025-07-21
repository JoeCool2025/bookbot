def get_book_text(path_to_file):
    file_contents = ""

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def book_length(path_to_file):
    book = get_book_text(path_to_file)
    words = book.split()

    return len(words)

def main():
    text = book_length("/home/adin-admin/boot_dev/bookbot/books/frankenstein.txt")
    print(f"{text} words found in the document")

main()
