def swap_columns():
    n, m = [int(i) for i in input("enter size of array:").split()]
    array = [[int(j) for j in input("enter row:").split()] for i in range(n)]
    i, j = [int(i) for i in input("which columns to swap:").split()]
    for k in range(len(array)):
        array[k][i], array[k][j] = array[k][j], array[k][i]
    print('\n'.join([' '.join([str(i) for i in row]) for row in array]))

swap_columns()