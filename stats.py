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

def split_dict(dict):
    return [{key: value} for key, value in dict.items()]

def get_count(dict):
    return list(dict.values())[0]

def sort_dict(dict):
    list = split_dict(dict)
    list.sort(reverse=True, key=get_count)
    return list
