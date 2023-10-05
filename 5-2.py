rows = 7
cols = 7

array = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        array[i][j] = 7 - i

for i in range(rows):
    for j in range(cols):
        print(array[i][j], end=' ')
    print()