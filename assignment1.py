"""
Broderick Thomsen, 29th March
Project details:

https://github.com/CP1404-2017-1/a1-BroderickWST
"""

# "You should be able to use generic, customisable functions to perform input with error checking"


def main():
    print("Reading List 1.0 - by Broderick Thomsen")
    file = open("books.csv", "r+")
    book_list = []
    print("{} books loaded from {}".format(len(load_book(book_list, file)), file.name))
    main_loop = 1  # consider renaming
    while main_loop != 0:
        menu_input = str(input("Menu:\nR - List required books\nC - List completed books\nA - Add new book\n"
                               "M - Mark a book as completed\nQ - Quit\n>>>"))
        if menu_input == "r" or menu_input == "R":
            print("Required books:")
            display_book(book_list, menu_input)
        elif menu_input == "c" or menu_input == "C":
            print("Completed books:")
            display_book(book_list, menu_input)
        elif menu_input == "a" or menu_input == "A":
            book_list = book_list + [add_book()]
            print("{} by {}, ({} pages) added to reading list".format(book_list[-1][0], book_list[-1][1],
                                                                      book_list[-1][2]))
        elif menu_input == "m" or menu_input == "M":
            print("Required books:")
            display_book(book_list, menu_input)
        elif menu_input == "q" or menu_input == "Q":
            main_loop = 0
            counter = 0  # consider renaming
            file.close()
            file = open("books.csv", "w")  # Not efficient. Doesn't work with adding books. Use seek() and truncate().
            for selection in book_list:  # consider renaming index
                separated_line = ",".join(selection)
                file.write(separated_line)
                counter += 1
            print("{} books saved to {}".format(counter, file.name))
            file.close()
        else:
            print("Invalid menu choice")
    print("Have a nice day :)")


def load_book(book_list, file):  # consider parameter names
    for row in file.readlines():
        book_list.append(row.split(","))
    return book_list


def display_book(book_list, menu_input):  # consider renaming function, parameters
    book_check = 0  # consider renaming
    num_pages = 0
    num_books = 0
    for selection, item in enumerate(book_list):  # consider renaming indexes
        if menu_input == "r" or menu_input == "R" or menu_input == "m" or menu_input == "M":
            if item[-1] == "r\n":
                print("{:>3}. {:<40} {:<20} {} pages".format(selection, (item[0]), (item[1]), (item[2])))  # turn into function?
                num_pages += int(item[2])
                num_books += 1
                book_check = 1
        elif menu_input == "c" or menu_input == "C":
            if item[-1] == "c\n":
                print("{:>3}. {:<40} {:<20} {} pages".format(selection, (item[0]), (item[1]), (item[2])))
                num_pages += int(item[2])
                num_books += 1
                book_check = 1
    if book_check == 0:
        print("No books")
    page_sum(num_books, num_pages, book_check)
    if menu_input == "m" or menu_input == "M":
        if book_check == 1:
            complete_book(book_list)


# Necessary? Would it be better suited if called from main, to justify existence?
def page_sum(total_books, total_pages, validation):
    if validation == 1:
        print("Total pages for {} books: {}".format(total_books, total_pages))


# returns a list that'll be appended to book_list when called as . . .
def add_book():
    loop = 1  # consider renaming
    title = str
    author = str
    pages = int
    while loop != 0:  # Can I put both Title and Author in a list, and then use a for loop to call them, so I only have to use the below process, once ?
        title = input("Title: ")
        if len(title) == 0 or title == " ":
            print("Input can not be blank")
        else:
            loop = 0
    loop = 1
    while loop != 0:
        author = input("Author: ")
        if len(author) == 0 or author == " ":
            print("Input can not blank")
        else:
            loop = 0
    loop = 1
    while loop != 0:
        try:
            pages = int(input("Pages: "))
            if pages >= 0:
                loop = 0
            else:
                print("Number must be >= 0")
        except ValueError:
            print("Invalid input; enter a valid number")
    new_book = [title, author, pages, "r\n"]
    return new_book


def complete_book(book_list):
    loop = 1
    print("Enter the number of a book to mark as completed")
    while loop != 0:
        try:
            marking_input = int(input(">>> "))  # consider renaming
            if book_list[marking_input][-1] == "c\n":
                print("That book is already completed")
                return
            elif marking_input >= 0 and book_list[marking_input][-1] != "c\n":
                book_list[marking_input][-1] = "c\n"
                print("{} by {} marked as completed".format(book_list[marking_input][0], book_list[marking_input][1]))
                return book_list
        except (ValueError, IndexError):
            print("Invalid input; enter a valid number")


if __name__ == '__main__':
    main()
