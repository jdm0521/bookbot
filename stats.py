def num_of_words(text):
    words = text.split()
    return len(words)


def num_each_char(text):
    text = text.lower()
    char_counts = {}
    
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def dict_print(char_and_count):
    char_list = [{"char": char, "num": count } for char, count in char_and_count.items()]
    
    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list
    
