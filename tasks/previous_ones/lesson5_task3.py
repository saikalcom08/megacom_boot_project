def two_dimensional_array(n):
    array = [[abs(i - j) for j in range(n)] for i in range(n)]
    for row in array:
        print(' '.join([str(i) for i in row]))
    return array

two_dimensional_array(10)