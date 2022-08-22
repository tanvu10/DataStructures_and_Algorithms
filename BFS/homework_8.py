from queue import Queue
row, col = map(int, (input().split(' ')))
matrix = [[] for _ in range(row)]
for ro in range(row):
    sub_row = list(input())
    matrix[ro] = sub_row

# print(matrix)
visited_matrix = [[0] * col for _ in range(row)]

count_dic = {}

total_sheep_left = 0
total_wolf_left = 0

for r in range(1,row-1):
    for c in range(1,col-1):
        sheep_count = 0
        wolf_count = 0
        if matrix[r][c] in ['.', 'k', 'v'] and visited_matrix[r][c] == 0:
            if matrix[r][c] == 'k':
                sheep_count += 1
            elif matrix[r][c] == 'v':
                wolf_count += 1
            else:
                pass
            qr = Queue()
            qc = Queue()
            qr.put(r)
            qc.put(c)
            visited_matrix[r][c] = 1
            mark = 0
            while not qr.empty():
                current_row = qr.get()
                current_col = qc.get()
                row_direction = [0, 1, -1, 0]
                col_direction = [-1, 0, 0, 1]
                for i in range(len(row_direction)):
                    near_row = current_row + row_direction[i]
                    near_col = current_col + col_direction[i]
                    if 0 <= near_row < row and 0 <= near_col < col:
                        if matrix[near_row][near_col] in ['.', 'k','v'] and visited_matrix[near_row][near_col] == 0:
                            if near_col == col -1 or near_col == 0 or near_row == 0 or near_row == row -1:
                                mark = 1
                            if matrix[near_row][near_col] == 'k':
                                sheep_count +=1
                            elif matrix[near_row][near_col] == 'v':
                                wolf_count +=1
                            else: pass

                            qr.put(near_row)
                            qc.put(near_col)
                            visited_matrix[near_row][near_col] = 1
            if mark == 1:
                total_wolf_left += wolf_count
                total_sheep_left += sheep_count
            else:
                if wolf_count >= sheep_count:
                    total_wolf_left += wolf_count
                elif wolf_count < sheep_count:
                    total_sheep_left += sheep_count

for nr in range(row):
    for nc in range(col):
        if (nr == 0 or nr == row - 1) :
            # print(r, c)
            if visited_matrix[nr][nc] == 0 :
                if matrix[nr][nc] == 'k':
                    total_sheep_left += 1
                elif matrix[nr][nc] == 'v':
                    total_wolf_left += 1
        else:
            if nc == 0 or nc == col -1:
                # print(r, c)
                if visited_matrix[nr][nc] == 0:
                    if matrix[nr][nc] == 'k':
                        total_sheep_left += 1
                    elif matrix[nr][nc] == 'v':
                        total_wolf_left += 1

print(total_sheep_left, total_wolf_left)