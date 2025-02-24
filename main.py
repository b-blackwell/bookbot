def main():
    from stats import get_num_words, get_book_text, character_check, sort_dict

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counts = character_check(text)
    sorted_counts = sort_dict(character_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_counts:
        for key in char:
            if key.isalpha():
                print(f"{key}: {char[key]}")
    print("============= END ===============")

main()
