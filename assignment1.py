"""
Broderick Thomsen, 29th March
Project details:

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
            new_book = [new_item("Title"), new_item("Author"), pages_entry(), "r\n"]
            books_list = books_list + [new_book]
            print("{} by {}, ({} pages) added to reading list".format(books_list[-1][0], books_list[-1][1],
                                                                      books_list[-1][2]))
        elif menu_input == "m":
            if book_check(books_list, menu_input):
                print("Required books:")
                display_books(books_list, menu_input)
                print("Enter the number of a book to mark as completed")
                mark_choice = verify_mark_num(books_list)
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
    books_list = []
    file = open("books.csv", "r")
    for row in file.readlines():
        books_list.append(row.split(","))
    file.close()
    return books_list


def book_check(books_list, mode):
    book_status = False
    for book in books_list:
        if book[-1] == "r\n":
            if mode == "r" or mode == "m":
                book_status = True
        elif book[-1] == "c\n" and mode == "c":
            book_status = True
    return book_status


def display_books(books_list, mode):
    num_pages = 0
    num_books = 0
    for book, item in enumerate(books_list):
        if item[-1] != "r\n":
            if mode == "r" or mode == "m":
                continue
        elif item[-1] != "c\n" and mode == "c":
            continue
        print("{:>3}. {:<40} {:<20} {} pages".format(book, (item[0]), (item[1]), item[2]))
        num_pages += int(item[2])
        num_books += 1
    print("Total pages for {} books: {}".format(num_books, num_pages))


def new_item(string):
    entry = input("{}: ".format(string))
    while len(entry) == 0 or len(entry.split()) == 0:
        print("Input can not be blank")
        entry = input("{}: ".format(string))
    return entry


def pages_entry():
    pages = -1
    while pages < 0:
        try:
            pages = int(input("Pages: "))
            if pages < 0:
                print("Number must be >= 0")
        except ValueError:
            print("Invalid input; enter a valid number")
    return str(pages)


def verify_mark_num(books_list):
    function_loop = True
    while function_loop:
        try:
            mark_choice = int(input(">>> "))
            if 0 <= mark_choice <= len(books_list) - 1:
                return mark_choice
        except (ValueError,IndexError):
            print("Invalid input; enter a valid number")
        print("Invalid input; enter a valid number")


def complete_book(books_list, mark_choice):
    books_list[mark_choice][-1] = "c\n"
    return books_list


def save_books(books_list):
    file = open("books.csv", "w")
    for book in books_list:
        book_string = ",".join(book)
        file.write(book_string)
    file.close()


if __name__ == '__main__':
    main()
