from stats import get_word_count

def get_book_text(book_filepath):
    with open(book_filepath) as book:
        return book.read()

def main():
    word_count = get_word_count(get_book_text("./books/frankenstein.txt"))
    print(f"{word_count} words found in the document")

main()
