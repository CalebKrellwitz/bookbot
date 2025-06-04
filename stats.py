def get_word_count(book):
    return len(book.split())

def get_character_counts(book):
    character_counts = {}
    lowered_book = book.lower()

    for char in lowered_book:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    
    return character_counts
