def read_book(file_path):
    with open(file_path) as file:
        contents = file.read()
    return contents

def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    contents = text.lower()
    char_count = {}
    for char in contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_characters(characters):
    test = {key: value for key, value in characters.items() if key.isalpha()}
    sorted_chars = sorted(test.items(), key=lambda item: item[1], reverse=True)
    return sorted_chars 

def report(x, y, z):
    print(f"--- Begin report of {x} ---")
    print(f"{y} words found in the document")
    for i in z:
        print(f"The '{i[0]}' character was found {i[1]} times")
    print("--- End report ---")

def main():
    book = "books/Frankenstein.txt"
    text = read_book(book)
    num_words = count_words(text)
    characters = character_count(text)
    chars_in_order = sort_characters(characters)
    report(book, num_words, chars_in_order)

main()
