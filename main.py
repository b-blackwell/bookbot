def main():
    from stats import get_num_words, get_book_text, character_check, sort_dict

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counts = character_check(text)
    sorted_counts = sort_dict(character_counts)
    print(f"{num_words} words found in the document")
    print(character_counts)
    print(sorted_counts)

main()
