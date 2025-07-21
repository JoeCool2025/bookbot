def book_word_count(path_to_file):
    book = ""

    with open(path_to_file) as f:
        book = f.read()
    
    words = book.split()

    return len(words)

def count_book_characters(path_to_file):
    book = ""
    characters = {}

    with open(path_to_file) as f:
        book = f.read()
        book = book.lower()

    for char in book:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters