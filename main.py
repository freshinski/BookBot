from stats import count_words, get_characters

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)

    num_words = count_words(text)
    print(f"Found {num_words} total words")

    char_counts = get_characters(text)
    print(char_counts)


main()