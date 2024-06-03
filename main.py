def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    filtered_chars_dict = filter_alphabetic_chars(chars_dict)
    char_list = convert_dict_to_list(filtered_chars_dict)

    def sort_on(element):
        return element["num"]
    
    char_list.sort(reverse=True, key=sort_on)

    print(f"{num_words} words found in the document")
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

def filter_alphabetic_chars(chars_dict):
    return {char: count for char, count in chars_dict.items() if char.isalpha()}

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def convert_dict_to_list(chars_dict):
    char_list = []
    for char, count in chars_dict.items():
        char_list.append({"char": char, "num": count})
    return char_list

main()