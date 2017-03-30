"""
Broderick Thomsen, 29th March
This file is to test the load_book function in a isolated file, as part of the planning phase. Multiple methods may be
tested, so this is why this file is seperate from the main file, as to avoid clutter.

https://github.com/CP1404-2017-1/a1-BroderickWST
"""


def main():
    file = open("temp.csv", "r")
    list_x = []
    a = 0
    for line in file.readlines():
        list_x.append([a, line.split(",")])
        a += 1

    # selection
    # print (list_x)
    # print (list_x[0])
    # print (list_x[0][0])
    # print (list_x[0][1])
    # print (list_x[0][1][1])

    # file = open("temp.csv", "r")
    # list_r = []
    # list_c = []
    # for line in file.readlines():
    #     line2 = line.split(",")
    #     if line2[-1] == "r\n":
    #         list_r += [line.split(",")]
    #     elif line2[-1] == "c\n":
    #         list_c += [line.split(",")]

    # important for formatting
    # print("This is list_c: {}\nThis is list_r: {}".format(list_c, list_r))
    # print("Hello, my name is {}, and I am the author of {}.".format(list_c[0][1],list_c[0][0]))

    # string = "Hello World, my name is Broderick Thomsen, What's yours, huh?"
    # string2 = string.replace(" ", "_")
    # list = string2.split(",")
    # print(list[1].replace("_", " "))

    # file = open("temp.csv", "r")
    # list_a = []
    # for line in file.readlines():
    #     list_a.append(line)
    #     print(list_a)

if __name__ == '__main__':
    main()