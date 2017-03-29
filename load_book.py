"""
Broderick Thomsen, 29th March
This file is to test the load_book function in a isolated file, as part of the planning phase. Multiple methods may be
tested, so this is why this file is seperate from the main file, as to avoid clutter.

https://github.com/CP1404-2017-1/a1-BroderickWST
"""


def main():
    file = open("temp.csv", "r")
    list_r = []
    list_c = []
    for line in file.readlines():
            if line[-1]=="r": # if and elif aren't working, refer to previous work
                list_r = line.split(",")
            elif line[-1]=="c":
                list_c = line.split(",")
    print ("This is list_c: {}\nThis is list_r: {}".format(list_c,list_r))



if __name__ == '__main__':
    main()

    # string = "Hello World, my name is Broderick Thomsen, What's yours, huh?"
    # string2 = string.replace(" ", "_")
    # list = string2.split(",")
    # print(list[1].replace("_", " "))

    # file = open("temp.csv", "r")
    # list_a = []
    # for line in file.readlines():
    #     list_a.append(line)
    #     print(list_a)