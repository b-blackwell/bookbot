def main():
    import sys
    from stats import get_num_words, get_book_text, character_check, sort_dict

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    character_counts = character_check(text)
    sorted_counts = sort_dict(character_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_counts:
        for key in char:
            if key.isalpha():
                print(f"{key}: {char[key]}")
    print("============= END ===============")

main()
