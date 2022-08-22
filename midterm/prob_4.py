from queue import Queue
while True:
    row_col = list(input().split())
    row = int(row_col[0])
    col = int(row_col[1])
    if row == 0 and col == 0:
        break
    # print(row,col)
    map = [['.']*col for _ in range(row)]
    # print(map)
    total_num_bomb = int(input())
    # print(total_num_bomb)
    for _ in range(total_num_bomb):
        list_bomb = list(input().split())
        # print(list_bomb)
        bomb_row = int(list_bomb[0])
        num_bomb = int(list_bomb[1])
        for bomb_col in list_bomb[2:]:
            map[bomb_row][int(bomb_col)] = '*'

    start = list(input().split())
    start_row = int(start[0])
    start_col = int(start[1])

    end = list(input().split())
    end_row = int(end[0])
    end_col = int(end[1])

    dist = [[0]*col for _ in range(row)]
    check_map = [[False]*col for _ in range(row)]
    q = Queue()
    q.put((start_row, start_col))
    check_map[start_row][start_col] = True
    row_direction = [0, -1, 1, 0]
    col_direction = [-1, 0, 0, 1]

    while not q.empty():
        current_row, current_col = q.get()
        for j in range(len(col_direction)):
            next_row = current_row + row_direction[j]
            next_col = current_col + col_direction[j]
            if 0 <= next_row < row and 0 <= next_col < col:
                if map[next_row][next_col] == '.' and check_map[next_row][next_col] == False:
                    check_map[next_row][next_col] = True
                    q.put((next_row, next_col))
                    dist[next_row][next_col] = dist[current_row][current_col] + 1
                    if next_row == end_row and next_col == end_col:
                        break

    print(dist[end_row][end_col])



