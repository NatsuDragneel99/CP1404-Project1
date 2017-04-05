"""
Broderick Thomsen, 29th March
Project details:

https://github.com/CP1404-2017-1/a1-BroderickWST
"""

# "You should be able to use generic, customisable functions to perform input with error checking"


FILE_NAME = "books.csv"


def main():
    print("Reading List 1.0 - by Broderick Thomsen")
    books_list = load_book()
    print("{} books loaded from {}".format(len(books_list), FILE_NAME))
    menu_input = str(input("Menu:\nR - List required books\nC - List completed books\nA - Add new book\n"
                           "M - Mark a book as completed\nQ - Quit\n>>>")).lower()
    while menu_input != "q":
        if menu_input == "r":
            if book_check(books_list, menu_input):
                print("Required books:")
            else:
                print("No books")

        elif menu_input == "c":
            if book_check(books_list, menu_input):
                print("Completed books:")
            else:
                print("No books")

        elif menu_input == "a":
            books_list = books_list + [add_book()]
            print("{} by {}, ({} pages) added to reading list".format(books_list[-1][0], books_list[-1][1],
                                                                      books_list[-1][2]))
        elif menu_input == "m":
            if book_check(books_list, menu_input):
                print("Required books:")
            else:
                print("No required books")
        else:
            print("Invalid menu choice")
        menu_input = str(input("Menu:\nR - List required books\nC - List completed books\nA - Add new book\n"
                               "M - Mark a book as completed\nQ - Quit\n>>>")).lower()
    # def save_books():
    file = open("books.csv", "w")
    books_string = ""  # swap  to old method of just writing to file from str(books_list), more efficient, less complex
    for book in books_list:
        book_string = ",".join(book)
        books_string += book_string
    file.seek(0)
    file.write(books_string)
    file.close()

    print("{} books saved to {}".format(len(books_list), FILE_NAME))
    print("Have a nice day :)")


def book_check(books_list, mode):
    book_status = False
    for book in books_list:
        if book[-1] == "r\n" and mode == "r" or mode == "m":
            book_status = True
        elif book[-1] == "c\n" and mode == "c":
            book_status = True
    return book_status


def load_book():
    book_list = []
    file = open("books.csv", "r+")
    for row in file.readlines():
        book_list.append(row.split(","))
    file.close()
    return book_list


def display_books(books_list, mode):  # consider renaming function (print_book), parameters
    list_content = False
    num_pages = 0
    num_books = 0
    for book, item in enumerate(books_list):
        if item[-1] != "r\n" and mode == "r" or mode == "m":
            continue
        elif item[-1] != "c\n" and mode == "c":
            continue
        print("{:>3}. {:<40} {:<20} {} pages".format(book, (item[0]), (item[1]), item[2]))
        num_pages += int(item[2])
        num_books += 1
        list_content = True
    if not list_content:
        print("No books")
    print("Total pages for {} books: {}".format(num_books, num_pages))


# def display_books(books_list, mode):  # consider renaming function (print_book), parameters
#     list_content = False  # consider renaming
#     num_pages = 0
#     num_books = 0
#     for book, item in enumerate(books_list):  # consider renaming indexes
#         if item[-1] == "r\n" and mode == "r" or mode == "m":
#             print("{:>3}. {:<40} {:<20} {} pages".format(book, (item[0]), (item[1]), item[2]))
#             num_pages += int(item[2])
#             num_books += 1
#             list_content = True
#         if item[-1] == "c\n" and mode == "c":
#             print("{:>3}. {:<40} {:<20} {} pages".format(book, (item[0]), (item[1]), (item[2])))
#             num_pages += int(item[2])
#             num_books += 1
#             list_content = True
#     if not list_content:
#         print("No books")
#     print("Total pages for {} books: {}".format(num_books, num_pages))


#
#     if mode == "m" or mode == "M":
#         if book_check == 1:
#             complete_book(book_list)


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
                pages = str(pages)
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
