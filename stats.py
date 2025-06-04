def get_character_counts(book):
    char_counts = {}
    lowered_book = book.lower()

    for char in lowered_book:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    return char_counts

def get_word_count(book):
    return len(book.split())

def sort_on(char_count):
    return char_count["count"]

def sort_character_counts(char_counts):
    char_counts_list = []

    for char in char_counts:
        char_dict = {
            "char": char,
            "count": char_counts[char]
        }
        char_counts_list.append(char_dict)

    char_counts_list.sort(reverse=True, key=sort_on)
    return char_counts_list
