from stats import get_word_count
from stats import get_character_counts

def get_book_text(book_filepath):
    with open(book_filepath) as book:
        return book.read()

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(book_text)
    character_counts = get_character_counts(book_text)

    print(f"{word_count} words found in the document")
    print(character_counts)

main()
