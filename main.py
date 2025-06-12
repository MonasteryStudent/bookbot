import sys
from stats import count_words, count_characters, sort_dict

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    num_words = count_words(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_char = count_characters(book)
    sorted_char = sort_dict(num_char)
    for elem in sorted_char:
        if elem["char"].isalpha():
            print(f"{elem["char"]}: {elem["num"]}")

main()