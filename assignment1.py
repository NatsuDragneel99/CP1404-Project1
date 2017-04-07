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
FUNCTION_LOOP = True


def main():
    print("Reading List 1.0 - by Broderick Thomsen")
    books_list = load_books()
    print("{} books loaded from {}".format(len(books_list), FILE_NAME))
    menu_input = str(input(MENU)).lower()
    while menu_input != "q":
        if menu_input == "r":
            print("Required books:")
            if book_check(books_list, menu_input):
                display_books(books_list, "r\n")
            else:
                print("No books")
        elif menu_input == "c":
            print("Completed books:")
            if book_check(books_list, menu_input):
                display_books(books_list, "c\n")
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
                display_books(books_list, "r\n")
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
    print("{} books saved to {}\nHave a nice day :)".format(len(books_list), FILE_NAME))


"""
    open books.csv as file_read for reading
    list_of_books = empty list
    for each row in file_read
        append row from file_read, to list_of_books
    close file_read
    return list_of_books
"""


def load_books():
    """
    load_books loads the information from the file and splits the contents of each row by their commas, it then appends
    the insides of the row to the list, list_of_books.
    """
    file_read = open("books.csv", "r")
    list_of_books = []
    for row in file_read.readlines():
        list_of_books.append(row.split(","))
    file_read.close()
    return list_of_books


"""
books_confirmation is False
for each book in books_list
    if book is required
        if mode is "r" or "m"
        books_confirmation is True
    if book is completed and mode is "c"
        books_confirmation is True
return books_confirmation
"""


def book_check(books_list, mode):
    """
    book_check makes sure the book_list has required or completed books in it, and if the mode is equivalent to the
    completion status of the book.
    """
    books_confirmation = False
    for book in books_list:
        if book[-1] == "r\n":
            if mode == "r" or mode == "m":
                books_confirmation = True
        elif book[-1] == "c\n" and mode == "c":
            books_confirmation = True
    return books_confirmation


"""
import operator
sort books_list by authors and then pages
for each book and book item of books_list
    if last item != "r\n" and mode is "r" or "m"
        continue
    otherwise if last item != "c\n" and mode is "c"
        continue
    books_string + book title, author and pages, \n
    count pages of book
    count book
books_string + total pages for books
return books_string
"""


def display_books(books_list, requirement):
    """
    display_books will sort the books_list, check if the user is searching for required or completed books, then print
    the books for the user's condition. The program will also keep track of the number of pages and books, and then
    print the total pages and books. Returns the books_list, now sorted.
    """
    import operator
    books_list.sort(key=operator.itemgetter(1, 2))
    num_pages = 0
    num_books = 0
    for book, item in enumerate(books_list):
        if item[-1] != requirement:
                continue
        print("{:>3}. {:<40} {:<20} {} pages".format(book, (item[0]), (item[1]), item[2]))
        num_pages += int(item[2])
        num_books += 1
    print("Total pages for {} books: {}".format(num_books, num_pages))
    return books_list


def add_item(string):
    """
    When called, add_item will make the user write a new string, with a length above zero.
    """
    item = input("{}: ".format(string))
    while len(item.split()) == 0:
        print("Input can not be blank")
        item = input("{}: ".format(string))
    return item


"""
while FUNCTION_LOOP is True
    try
        get pages as int
        if pages less than than 0
            display pages must be 0 or greater
    except on ValueError
        display bad input
    return pages as string
"""


def add_pages():
    """
    add_pages will ask the user for the number of pages of their new book, and then error-test the input to make sure
    it's an integer. The input is then tested to be over, or equal to 0, and if so, the function will return pages as a
    string.
    """
    while FUNCTION_LOOP:
        try:
            pages = int(input("Pages: "))
            if pages < 0:
                print("Number must be >= 0")
            else:
                return str(pages)
        except ValueError:
            print("Invalid input; enter a valid number")


def verify_mark_choice(books_list):
    while FUNCTION_LOOP:
        try:
            mark_choice = int(input(">>> "))
            if 0 <= mark_choice <= len(books_list) - 1:
                return mark_choice
            else:
                print("Invalid input; enter a valid number")
        except (ValueError, IndexError):
            print("Invalid input; enter a valid number")


"""
last item of chosen_book in books_list = "c\n"
return books_list
"""


def complete_book(books_list, chosen_book):
    """
    complete_book will mark the final item in the chosen book of the books_list, as "c\n". It will then return the list
    with the chosen book, marked.
    """
    books_list[chosen_book][-1] = "c\n"
    return books_list

"""
    open books.csv as file_write for writing
    for each book in books_list
        convert whitespace of book to comma, under book_string
        write book_string to file_write
    close file_write
"""


def save_books(books_list):
    """
    save_books will open the books.csv file in write mode, and for every book in the books_list, it will join the book
    by its entries, with commas, and save them in a variable called books_string. books_string is then written to the
    file. The file will close at the end of the function.
    """
    file_write = open("books.csv", "w")
    for book in books_list:
        book_string = ",".join(book)
        file_write.write(book_string)
    file_write.close()


if __name__ == '__main__':
    main()
