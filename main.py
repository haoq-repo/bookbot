def open_book(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def word_count(contents):
    words = contents.split()
    return len(words)

def main():
    bookpath = "books/frankenstein.txt"
    content = open_book(bookpath)
    print(word_count(content))

main()