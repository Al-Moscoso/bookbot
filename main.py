
def character_count(file_contents):
    lower_case_file_contents = file_contents.lower()
    character_dict = dict()
    for c in lower_case_file_contents:
        if c in character_dict.keys():
            character_dict[c] += 1
        else:
            character_dict[c] = 1
    return character_dict


def print_report(characters, words ):

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")

    for k,v in characters.items():
        if k.isalpha():
            print(f"The \'{k}\' character was found {v} times")

    print("--- End report ---")


def word_count(file_contents):
    return len(file_contents.split())

def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)

    words = word_count(file_contents)
    # print(words)
    
    characters = character_count(file_contents)
    # print(characters)

    print_report(characters, words)


main()

