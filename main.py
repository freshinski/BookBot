import sys
from stats import count_words, get_characters, sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")

    num_words = count_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    char_counts = get_characters(text)

    sorted_chars = sorted_list(char_counts)
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
   

    print("============= END ===============")

main()