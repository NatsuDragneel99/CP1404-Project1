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
    while program_loop != 0:
        print("Menu:\nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ - Quit")
        menu_input = str(input(">>> "))
        if menu_input == "r" or menu_input == "R": # TODO: "Required books:" or "None"
            page_sum = 0  # gotta be a better way to count pages
            num_books = 0  # this could be in a list - make required reading into a list and return that from display books so can be used for "Required Books" and to easily count how many required books there are. You can return it back to the main list when done so changes are always accounted for, or maybe just do that when marking/adding a book.
            display_book(book_list, menu_input, page_sum, num_books)
        elif menu_input == "c" or menu_input == "C": # TODO: "Completed books:" or "None"
            page_sum = 0
            num_books = 0
            display_book(book_list, menu_input, page_sum, num_books)
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
        else:
            print("Invalid menu choice")


def load_book(book_list, file):
    for line in file.readlines():
        book_list.append(line.split(","))
    return book_list

# (rename func) or (isolate page_sum into own func and call from main)
def display_book(book_list, menu_input, pages, num_books):
    for selection, i in enumerate(book_list):
        if menu_input == "r":
            if i[-1] == "r\n":
                print("{:>3}. {:<40} {:<20} {} pages".format(selection, (i[0]), (i[1]), (i[2])))
                pages += int(i[2])
                num_books += 1
        if menu_input == "c":
            if i[-1] == "c\n":
                print("{:>3}. {:<40} {:<20} {} pages".format(selection, (i[0]), (i[1]), (i[2])))
                pages += int(i[2])
                num_books += 1
    page_sum(num_books, pages)


# Neccessary? Would it be better suited if called from main?
def page_sum(num_books, page_sum):
    print("Total pages for {} books: {}".format(num_books, page_sum))


#returns a list that'll be appended to book_list when called as . . .
def add_book():
    print("ok")


if __name__ == '__main__':
    main()
