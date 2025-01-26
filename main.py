def open_book(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def word_count(contents):
    words = contents.split()
    return len(words)

def character_counter(contents):
    character_dict = {}
    lowered_string = contents.lower()
    for i in lowered_string:
        if i in character_dict:
            count = character_dict[i] + 1
            character_dict[i] = count
        else:
            character_dict[i] = 1
    

    return character_dict
            
def main():
    bookpath = "books/frankenstein.txt"
    content = open_book(bookpath)

    print(f"--- Begin report of {bookpath} ---")

    words = word_count(content)
    print(f"{words} words found in the document")

    char_dict = character_counter(content)
    for char in char_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {char_dict[char]} times")
    
    print("--- End report ---")

main()