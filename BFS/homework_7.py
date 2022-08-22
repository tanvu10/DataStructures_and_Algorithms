from queue import Queue
row, col = map(int, (input().split(' ')))
matrix = [[] for _ in range(row)]
for r in range(row):
    sub_row = list(input())
    matrix[r] = sub_row

start_row, start_col =  map(int, input().split(' '))
des_row, des_col = map(int, input().split(' '))
start_row, start_col = start_row -1, start_col- 1
des_row, des_col  = des_row - 1, des_col -1
# print(start_row, start_col)
# print(matrix)


def bug_(matrix, start_row, start_col, des_row , des_col):
    visited_matrix = [[0]*col for _ in range(row)]
    # print(visited_matrix)
    visited_matrix[start_row][start_col] = 1
    qr = Queue()
    qc = Queue()
    qr.put(start_row)
    qc.put(start_col)
    row_direction = [0, 1, -1, 0]
    col_direction = [-1, 0, 0, 1]
    while not qr.empty():
        current_row = qr.get()
        current_col = qc.get()
        while matrix[current_row][current_col] == 'X':
            current_row  = current_row +1
            if current_row > row -1:
                return print('NO')

        for i in range(len(row_direction)):
            near_row = current_row + row_direction[i]
            near_col = current_col + col_direction[i]
            if near_row == des_row and near_col == des_col:
                return print('YES')
            if 0 <= near_col < col and 0 <= near_row < row:
                if matrix[near_row][near_col] != 'X' and visited_matrix[near_row][near_col] == 0:
                    visited_matrix[near_row][near_col] = 1
                    qr.put(near_row)
                    qc.put(near_col)
            else:
                pass

    print('NO')






bug_(matrix,start_row, start_col, des_row , des_col )
