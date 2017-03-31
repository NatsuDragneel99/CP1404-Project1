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
            if book_list[-1] != "r" or book_list[-1] != "R":
                print("Required books:")
                for selection, i in enumerate(book_list):
                    display_book(i, selection)
            else:
                print("None.")
            # display_book(book_list, menu_input)
            # After books have been presented, use page_count with these books to count pages, return int to display
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


def display_book(i, selection):
    if i[-1] == "r\n":
        return print("{:>3}. {:<40} {:<20} {} pages".format(selection, (i[0]), (i[1]), (i[2])))


# print("This is object {} in book_list, it contains: {}".format(selection, book_list))
# print("{}".format(i[-1]))


if __name__ == '__main__':
    main()
