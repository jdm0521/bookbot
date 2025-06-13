import sys
from stats import num_of_words, num_each_char, dict_print

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)  # Relative path
    words_num = num_of_words(book_text)
    print(f'{words_num} words found in the document')
    each_character = num_each_char(book_text)
    dict_pretty = dict_print(each_character)
    sorted_characters = dict_pretty
    print(dict(list(each_character.items())[:10]))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_text}")
    print("----------- Word Count ----------")
    print(f'Found {words_num} total words')
    print("--------- Character Count -------")
    for item in sorted_characters:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
