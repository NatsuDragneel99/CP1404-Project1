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
        if menu_input == "r" or menu_input == "R":
            print("0")
            # List required books
        elif menu_input == "c" or menu_input == "C":
            print("1")
            # List completed books
        elif menu_input == "a" or menu_input == "A":
            print("2")
            # Add new book
        elif menu_input == "m" or menu_input == "M":
            print("3")
            # Mark a book as completed
        elif menu_input == "q" or menu_input == "Q":
            print("4")
            # Quit
            program_loop = 0


def load_book(book_list, file):
    for line in file.readlines():
        book_list.append(line.split(","))
    return book_list


def display_book(book_list, menu_input):
    if menu_input == "r" or menu_input == "R":
        for letter in book_list:
            if letter[-1] == "r":
                print ("OK") # 0. Title, Author, Pages
                # append page number to new list, forward that list to page_count() (this should reset each rotation)



if __name__ == '__main__':
    main()
