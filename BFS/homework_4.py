# import numpy as np
from queue import Queue
test_num = int(input())
i = 0
while i < test_num:
    dimension = input().split(' ')
    C, R = int(dimension[0]), int(dimension[1])
    # print(C, R)
    # matrix = np.zeros((R, C),dtype=str)
    matrix = [[]*C for _ in range(R)]
    start_row = 0
    start_col = 0
    for r in range(R):
        Ci = list(input())
        if '@' in Ci:
            start_col = Ci.index('@')
            start_row = r
        # print(Ci)
        # matrix[r,:] = np.array(Ci).reshape(1,-1)
        matrix[r] = Ci
    # print(matrix)
    # print(start_row)
    # print(start_col)
    # visited_matrix = np.zeros((R, C))
    visited_matrix = [[0]*C for _ in range(R)]

    qr = Queue()
    qc = Queue()
    qr.put(start_row)
    qc.put(start_col)
    visited_matrix[start_row][start_col] = 1

    # print(visited_matrix)
    row_direction = [0, -1, 1, 0]
    col_direction = [-1, 0, 0, 1]

    count = 0
    while not qr.empty():
        count += 1
        col_index = qc.get()
        row_index = qr.get()

        for k in range(len(row_direction)):
            near_row_index = row_index + row_direction[k]
            near_col_index = col_index + col_direction[k]
            # if 0 <= near_row_index <  visited_matrix.shape[0] and 0 <= near_col_index <  visited_matrix.shape[1]:
            if 0 <= near_row_index < R and 0 <= near_col_index < C:
                if matrix[near_row_index][near_col_index] == '#':
                    pass
                else:
                    # check visited:
                    if visited_matrix[near_row_index][near_col_index] == 0:
                        visited_matrix[near_row_index][near_col_index] = 1
                        qr.put(near_row_index)
                        qc.put(near_col_index)
                        # print(visited_matrix)
            else:
                pass

    # print(visited_matrix)
    print(f'Case {i+1}: {count}')
    i += 1
