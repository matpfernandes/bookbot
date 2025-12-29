import sys
from stats import words_count, character_count, order_characters

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print("============ BOOKBOT ============")
    book_name = sys.argv[1]
    print(f"Analyzing book found at {book_name}...")
    
    book = get_book_text(book_name)

    print("----------- Word Count ----------")
    words = words_count(book)
    print(f"Found {words} total words")

    print("--------- Character Count -------")
    characters = order_characters(character_count(book))

    for c in characters:
        if not c["char"].isalpha():
            continue

        print(f"{c['char']}: {c['num']}")


main()