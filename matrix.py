def main():
    """-------------------------------------------------------------------+
    | Draw squares with number inside. Sum of each row and column's items |
    | must be equal. For example if given 3, the square should look like: |
    | Size 3                                                              |
    | +---+---+---+                                                       |
    | │ 8 │ 1 │ 6 │ – 15                                                  |
    | +---+---+---+                                                       |
    | │ 3 │ 5 │ 7 │ – 15                                                  |
    | +---+---+---+                                                       |
    | │ 4 │ 9 │ 2 │ – 15                                                  |
    | +---+---+---+                                                       |
    |   |   |   |                                                         |
    |  15  15  15                                                         |
    +---------------------------------------------------------------------+
    """

    print('Enter size of matrix: ')
    size = input()
    generate_table(int(size))


def generate_table(size):
    """----------------------------------------------------+
    | Generate the table, first make empty table then fill |
    | it with numbers. Also try to do simple test.         |
    +------------------------------------------------------+
    """
    if size < 3 or size % 2 != 1:
        print('Minimum size is 3 and must be odd. Please re-enter.\n')
        main()
    matrix = generate_empty(size)
    filled = filling(matrix, size)
    test = [0] * size
    for i in range(0, size):
        print_sep(size)
        print_col(filled[i])
        for j in range(0, size):
            test[i] += filled[i][j]
    print_sep(size)
    if (test[0] == test[size-1] == test[int((size - 1)/2)]):
        print('Sum each row: ', test[0])
    print("\n")
    main()


def filling(matrix, size):
    """----------------------------------------------------------+
    | Function handles the filling numbers into correct position |
    | task. Accept empty matrix and return the filled matrix.    |
    +------------------------------------------------------------+
    """
    init = int((size - 1)/2)
    maxNum = size * size + 1
    x = 0
    y = init
    for i in range(1, maxNum):
        if i == 1:
            matrix[x][init] = 1
        if 1 < i < maxNum:
            matrix[x][y] = i
        next = checking(x-1, y+1, size, matrix)
        x = next[0]
        y = next[1]
    return matrix


def checking(x, y, size, matrix):
    """-----------------------+
    | Check the next position |
    +-------------------------+
    """
    if (x < 0 and y < size):  # out top border
        return [size - 1, y]
    if (x < 0 and y == size):  # stuck at the top right corner
        return [x + 2, y - 1]
    if (x < size and y == size):  # out of right border
        return [x, 0]
    if (x < size-1 and matrix[x][y] != 0):  # still inside, but stuck next step
        return [x+2, y-1]
    return [x, y]  # nothing there, just fill


def generate_empty(size):
    """------------------------------------+
    | Generate empty table and fill with 0 |
    +--------------------------------------+
    """
    matrix = [0] * size
    for i in range(0, size):
        row = [0] * size
        matrix[i] = row
    return matrix


def print_sep(size):
    """----------------------------------------+
    | Function handle drawing the horizon line |
    +------------------------------------------+
    """
    numChar = len(str(size * size))
    print(("+-" + "-" * numChar + "-") * size + "+")


def print_col(row):
    """--------------------------------------------+
    | Drawing the vertical line with number inside |
    +----------------------------------------------+
    """
    size = len(row)
    cells = ""
    for i in range(0, size):
        cells += ("│ " + space(row[i], size) + str(row[i]) + " ")
    print(cells + "│")


def space(current, size):  #
    """--------------------------------------------------+
    | Detect current number and add space(s) in front of |
    | it to align number and have better visual          |
    +----------------------------------------------------+
    """
    numChar = len(str(size * size))
    numCurr = len(str(current))
    return " " * (numChar - numCurr)


main()
