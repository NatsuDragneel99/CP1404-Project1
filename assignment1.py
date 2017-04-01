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
    program_loop = 1
    while program_loop != 0:
        print("Menu:\nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ - Quit")
        menu_input = str(input(">>> "))
        if menu_input == "r" or menu_input == "R":
            print("Required books:")
            display_book(book_list, menu_input)
        elif menu_input == "c" or menu_input == "C":
            print("Completed books:")
            display_book(book_list, menu_input)
        elif menu_input == "a" or menu_input == "A":
            book_list = book_list + [add_book()]
            print("{} by {}, ({} pages) added to reading list".format(book_list[-1][0], book_list[-1][1], book_list[-1][2]))
        elif menu_input == "m" or menu_input == "M":
            print("Required books:")
            display_book(book_list, menu_input)
        elif menu_input == "q" or menu_input == "Q":
            program_loop = 0
            b = 0
            file.close()
            file = open("temp.csv", "w") # Whilst this works, it's not as efficient as it can be. Need to fix.
            for line in book_list:
                v = ",".join(line)
                file.write(v)
                b += 1
            print("{} books saved to {}".format(b, file.name))
            file.close()
        else:
            print("Invalid menu choice")
    print("Have a nice day :)")


def load_book(book_list, file):
    for line in file.readlines():
        book_list.append(line.split(","))
    return book_list


# rename function?
def display_book(book_list, menu_input):
    y = 0
    pages = 0
    books = 0
    for selection, i in enumerate(book_list):
        if menu_input == "r" or menu_input == "R" or menu_input == "m" or menu_input == "M":
            if i[-1] == "r\n":
                print("{:>3}. {:<40} {:<20} {} pages".format(selection, (i[0]), (i[1]), (i[2]))) #turn into function
                pages += int(i[2])
                books += 1
                y = 1
        elif menu_input == "c" or menu_input == "C":
            if i[-1] == "c\n":
                print("{:>3}. {:<40} {:<20} {} pages".format(selection, (i[0]), (i[1]), (i[2])))
                pages += int(i[2])
                books += 1
                y = 1
    if y == 0:
        print("No books")
    page_sum(books, pages, y)
    if menu_input == "m" or menu_input == "M":
        if y == 1:
            complete_book(book_list)


# Necessary? Would it be better suited if called from main, to justify existence?
def page_sum(num_books, total_pages, y):
    if y == 1:
        print("Total pages for {} books: {}".format(num_books, total_pages))


# returns a list that'll be appended to book_list when called as . . .
def add_book():
    loop = 1
    title = str
    author = str
    pages = int
    while loop != 0:
        title = input("Title: ")
        if len(title) == 0 or title == " ":
            print("Input can not be blank")
        else:
            loop = 0
    loop = 1
    while loop !=0:
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
    x = -1
    print("Enter the number of a book to mark as completed")
    while loop != 0:
        try:
            x = int(input(">>> "))
            if book_list[x][-1] == "c\n":
                print("That book is already completed")
                return
            elif x >= 0 and book_list[x][-1] != "c\n":
                book_list[x][-1] = "c\n"
                print("{} by {} marked as completed".format(book_list[x][0], book_list[x][1]))
                return book_list
        except (ValueError, IndexError):
            print("Invalid input; enter a valid number")


if __name__ == '__main__':
    main()
