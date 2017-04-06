"""
Broderick Thomsen, 7th April 2017
Project details:
    This project is a simple reading list that allows users to keep track of their personal library, by adding the books
    they need to read, and saving books they have read, to a file. The program can recount these details back to the
    user, in addition to the total number of pages per book the user has read and pages they need to read.

https://github.com/CP1404-2017-1/a1-BroderickWST
"""

FILE_NAME = "books.csv"
MENU = "Menu:\nR - List required books\nC - List completed books" \
       "\nA - Add new book\nM - Mark a book as completed\nQ - Quit\n>>> "


def main():
    print("Reading List 1.0 - by Broderick Thomsen")
    books_list = load_books()
    print("{} books loaded from {}".format(len(books_list), FILE_NAME))
    menu_input = str(input(MENU)).lower()
    while menu_input != "q":
        if menu_input == "r":
            print("Required books:")
            if book_check(books_list, menu_input):
                display_books(books_list, menu_input)
            else:
                print("No books")
        elif menu_input == "c":
            print("Completed books:")
            if book_check(books_list, menu_input):
                display_books(books_list, menu_input)
            else:
                print("No books")
        elif menu_input == "a":
            new_book = [add_item("Title"), add_item("Author"), add_pages(), "r\n"]
            books_list = books_list + [new_book]
            print("{} by {}, ({} pages) added to reading list".format(books_list[-1][0], books_list[-1][1],
                                                                      books_list[-1][2]))
        elif menu_input == "m":
            if book_check(books_list, menu_input):
                print("Required books:")
                display_books(books_list, menu_input)
                print("Enter the number of a book to mark as completed")
                mark_choice = verify_mark_choice(books_list)
                if books_list[mark_choice][-1] == "r\n":
                    complete_book(books_list, mark_choice)
                    print("{} by {} marked as completed".format(books_list[mark_choice][0], books_list[mark_choice][1]))
                else:
                    print("That book is already completed")
            else:
                print("No required books")
        else:
            print("Invalid menu choice")
        menu_input = str(input(MENU)).lower()
    save_books(books_list)
    print("{} books saved to {}".format(len(books_list), FILE_NAME))
    print("Have a nice day :)")


def load_books():
    """
    open books.csv as file_read for reading
    for each row in file_read
        append row from file_read, to list_of_books
    close file_read
    return list_of_books
    """
    list_of_books = []
    file_read = open("books.csv", "r")
    for row in file_read.readlines():
        list_of_books.append(row.split(","))
    file_read.close()
    return list_of_books


def book_check(books_list, mode):
    """
    books_confirmation is False
    for each book in books_list
        if book is required and if mode is "r" or "m"
            books_confirmation is True
        if book and mode is completed
            books_confirmation is True
    return books_confirmation
    """
    books_confirmation = False
    for book in books_list:
        if book[-1] == "r\n":
            if mode == "r" or mode == "m":
                books_confirmation = True
        elif book[-1] == "c\n" and mode == "c":
            books_confirmation = True
    return books_confirmation


def display_books(books_list, mode):
    """
    for each book and book item of books_list
        if last item != "r\n" and mode is "r" or "m"
            continue
        otherwise if last item != "c\n" and mode is "c"
            continue
        display book title, author and pages
        count pages of book
        count book
    display total pages for total books
    """
    num_pages = 0
    num_books = 0
    for book, item in enumerate(books_list):
        if item[-1] != "r\n":
            if mode == "r" or mode == "m":
                continue
        elif item[-1] != "c\n" and mode == "c":
            continue
        print("{:>3}. {:<41} by {:<20} {} pages".format(book, (item[0]), (item[1]), item[2]))
        num_pages += int(item[2])
        num_books += 1
    print("Total pages for {} books: {}".format(num_books, num_pages))


def add_item(string):
    item = input("{}: ".format(string))
    while len(item.split()) == 0:
        print("Input can not be blank")
        item = input("{}: ".format(string))
    return item


def add_pages():
    """
    while pages less than 0
        try
            get pages as int
            if pages less than than 0
                display pages must be 0 or greater
        except on ValueError
            display bad input
        return pages as string
    """
    pages = -1
    while pages < 0:
        try:
            pages = int(input("Pages: "))
            if pages < 0:
                print("Number must be >= 0")
        except ValueError:
            print("Invalid input; enter a valid number")
    return str(pages)


def verify_mark_choice(books_list):
    function_loop = True
    while function_loop:
        try:
            mark_choice = int(input(">>> "))
            if 0 <= mark_choice <= len(books_list) - 1:
                return mark_choice
            else:
                print("Invalid input; enter a valid number")
        except (ValueError, IndexError):
            print("Invalid input; enter a valid number")


def complete_book(books_list, chosen_book):
    """
    last item of chosen_book in books_list = "c\n"
    return books_list
    """
    books_list[chosen_book][-1] = "c\n"
    return books_list


def save_books(books_list):
    """
    open books.csv as file_write for writing
    for each book in books_list
        convert whitespace of book to comma, under book_string
        write book_string to file_write
    close file_write
    """
    file_write = open("books.csv", "w")
    for book in books_list:
        book_string = ",".join(book)
        file_write.write(book_string)
    file_write.close()


if __name__ == '__main__':
    main()
