"""
Broderick Thomsen, 29th March
Project details:

https://github.com/CP1404-2017-1/a1-BroderickWST
"""


def main():
    print("Reading List 1.0 - by Broderick Thomsen")
    file = open("temp.csv", "r+")
    book_list = []
    print("{} books loaded from {}".format(len(load_book(book_list, file)), file.name))
    program_loop = 1  # This method of looping is subject to change
    while program_loop == 1:
        print("Menu:\nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ - Quit")
        menu_input = str(input(">>> "))
        if menu_input == "q" or menu_input == "Q":
            program_loop = 0


def load_book(book_list, file):
    for line in file.readlines():
        book_list.append(line.split(","))
    return book_list


if __name__ == '__main__':
    main()
