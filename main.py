import stats

def get_book_text(book_filepath):
    with open(book_filepath) as book:
        return book.read()

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = stats.get_word_count(book_text)
    character_counts = stats.get_character_counts(book_text)
    sorted_character_counts = stats.sort_character_counts(character_counts)

    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------")

    for character in sorted_character_counts:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["count"]}")
    
    print("============= END ===============")

main()
