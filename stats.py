def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_characters(text):
    counts = {}
    for characters in text:
        characters = characters.lower()
        if characters in counts:
            counts[characters] += 1
        else:
            counts[characters] = 1
    return counts

