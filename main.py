def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    print(f"Found {num_words} total words")


main()