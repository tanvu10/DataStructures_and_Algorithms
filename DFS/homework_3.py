row, col, required_num_lake = map(int, input().split(' '))
matrix = []
for _ in range(row):
    some_row = list(input())
    matrix.append(some_row)
# print(matrix)

def DFS(matrix, col, row):
    visited = [[False]*col for _ in range(row)]
    # print(visited)
    dr = [0,-1,1,0]
    dc = [-1,0,0,1]
    lake_track_dic = {}
    # print(row, col)
    count_lake = 0
    lake_list_index_dic = {}
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == '.' and visited[r][c] == False:
                sub_index_list = []
                sub_index_list.append([r,c])
                sea_connected = False
                if c == col - 1 or c == 0 or r == row - 1 or r == 0:
                    sea_connected = True
                area = 1
                stack = []
                stack.append((r,c))
                visited[r][c] = True
                while len(stack) > 0:
                    current_row, current_col = stack.pop()
                    for i in range(len(dr)):
                        next_row = current_row + dr[i]
                        next_col = current_col + dc[i]
                        if 0 <= next_col < col and 0 <= next_row < row\
                            and matrix[next_row][next_col] == '.' and visited[next_row][next_col] == False:
                            if next_col == col-1 or next_col == 0 or next_row == row-1 or next_row ==0:
                                sea_connected = True
                            sub_index_list.append([next_row, next_col])
                            area += 1
                            visited[next_row][next_col] = True
                            stack.append((next_row,next_col))

                if not sea_connected:
                    if area in lake_track_dic.keys():
                        lake_track_dic[area] += 1
                        lake_list_index_dic[area].append(sub_index_list)
                    else:
                        lake_track_dic[area] = 1
                        lake_list_index_dic[area] = []
                        lake_list_index_dic[area].append(sub_index_list)
                    count_lake += 1



    # print(count_lake)
    # print(lake_track_dic)
    num_remove = 0
    num_water = 0
    if count_lake == required_num_lake:
        print(num_remove)
        for ro in range(row):
            print(''.join(matrix[ro]))
    else:
        if len(lake_track_dic.keys()) > 0:
            for key in sorted(lake_track_dic.keys()):
                while lake_track_dic[key] > 0:
                    lake_track_dic[key] -= 1
                    count_lake -= 1
                    num_remove += 1
                    num_water += key
                    current_lake_index = lake_list_index_dic[key].pop()
                    for all_index in current_lake_index:
                        matrix[all_index[0]][all_index[1]] = '*'

                    if count_lake == required_num_lake:
                        print(num_water)
                        for ro in range(row):
                            print(''.join(matrix[ro]))
                            # print(*matrix[ro])
                        return
DFS(matrix, col, row)


# print(lake_track_dic)
# print(lake_list_index_dic)