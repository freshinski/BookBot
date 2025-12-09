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

def sort_on(characters):
    return characters["num"]

def sorted_list(counts):
    empty_list = []
    for key in counts:
        characters = counts[key]
        empty_list.append({"char": key, "num": characters})
    empty_list.sort(reverse=True, key=sort_on)
    return empty_list


