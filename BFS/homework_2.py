from queue import Queue
num_cases = int(input())
def bug_(matrix, num_row, num_col):
    #check for 2 gates:
    # print(num_row)
    # print(num_col)
    if num_row == 1 and num_col == 1:
        return print('invalid')

    visited_matrix = [[0]*col for _ in range(row)]

    def find_start(matrix, num_row, num_col):
        row_list = []
        col_list = []
        for r in range(num_row):
            for c in range(num_col):
                if (r == 0 or r == num_row - 1) :
                    # print(r, c)
                    if matrix[r][c] == '.':
                        row_list.append(r)
                        col_list.append(c)
                else:
                    if c == 0 or c == num_col -1:
                        # print(r, c)
                        if matrix[r][c] == '.':
                            row_list.append(r)
                            col_list.append(c)
        if len(row_list) == 2:
            return row_list[0], col_list[0]
        else:
            return 'invalid'

    # print(row_list)
    # print(col_list)
    if find_start(matrix, num_row, num_col) == 'invalid':
        return print('invalid')
    else:
        start_row, start_col = find_start(matrix, num_row, num_col)
        # print(start_row,start_col)
        qr = Queue()
        qc = Queue()
        qr.put(start_row)
        qc.put(start_col)
        visited_matrix[start_row][start_col] =1
        row_direction = [0, -1, 1, 0]
        col_direction = [-1, 0, 0, 1]
        end_count = 0
        while not qr.empty():
            current_row = qr.get()
            current_col = qc.get()
            for j in range(len(col_direction)):
                next_row = current_row + row_direction[j]
                next_col = current_col + col_direction[j]
                if 0 <= next_row < num_row and 0 <= next_col < num_col:
                    if matrix[next_row][next_col] == '.' and visited_matrix[next_row][next_col] == 0:
                        if next_row == num_row - 1 or next_row == 0 or next_col == 0 or next_col == num_col -1:
                            # print(next_row, next_col)
                            end_count+=1
                        qr.put(next_row)
                        qc.put(next_col)
                        visited_matrix[next_row][next_col] = 1
        # print(end_count)
        if end_count == 1:
            return print('valid')
        return print('invalid')

for _ in range(num_cases):
    row, col = map(int, input().split(' '))
    # print(row, col)
    matrix = [[] for _ in range(row)]
    for ro in range(row):
        matrix[ro] = (list(input()))
    # print(matrix)
    bug_(matrix, row, col)