def main():
    print('Enter size of square: ')
    size = input()
    draw_table(int(size))


def draw_table(size):  # main function
    """ Draw square with number inside.
    For example if given 3, the square should look like
    1 - 2 - 3
    4 - 5 - 6
    7 - 8 - 9
    """
    if size < 1:
        print('Minimum size of quare is 1.\n')
        main()  # Reset
    for x in range(0, size):
        print_sep(size)
        print_col(x, size)
    print_sep(size)

    # Reset
    print("\n")
    main()


def print_sep(size):  # Function handle drawing the horizon line
    numChar = len(str(size * size))
    print(("+-" + "-" * numChar + "-") * size + "+")


def print_col(x, size):  # Drawing the vertical line with number inside
    cells = ""
    for y in range(0, size):
        curr = x * size + y + 1
        cells += ("│ " + space(curr, size) + str(curr) + " ")
    print(cells + "│")


def space(current, size):  # create space in front of number
    numChar = len(str(size * size))
    numCurr = len(str(current))
    return " " * (numChar - numCurr)


main()
