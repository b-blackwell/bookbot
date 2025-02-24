def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def character_check(text):
    character_counts = {}
    lowered_text = text.lower()
    for character in lowered_text:
        character_counts[character] = character_counts.get(character, 0) + 1
    return character_counts

def sort_dict(dict):
    sorted_dict = []
    sorted_dict = dict.split()
    sorted_dict.sort(reverse=True, key=sorted_dict)
    return sorted_dict["num"]
