from queue import Queue

def solve(a):
    s_row = sum(a[0])
    s_col = sum([a[_][0] for _ in range(len(a))])
    for i in range(1, len(a)):
        if sum(a[i]) != s_row or sum([a[_][i] for _ in range(len(a))]) != s_col:
            return False
    return True

def main(B):
    big_list = []
    if not solve(B):
        print(-1)
        return
    count = 0
    while B != [[0] * n] * n and  count < 2500:
        small_list = [0] * (n+1)
        count += 1
        check = [False]*n
        coordinate_row = {}  # key is col, value is row
        visited = [[False] * n for _ in range(n)]
        queue_visited = [[False] * n for _ in range(n)]
        q = Queue()

        for i in range(n):
            if B[i][i] == 0:
                q.put((i, i))
                queue_visited[i][i] = True
            else:
                check[i] = True
            visited[i][i] = True
            coordinate_row[i] = i

        while not q.empty() and sum(check) != n:
            cur_row, cur_col = q.get()
            for sub_col in range(n):
                if B[cur_row][sub_col] != 0 and not visited[cur_row][sub_col]:
                    if coordinate_row[sub_col] != cur_row:
                        check[sub_col] = True
                        if sum(check) != n and not queue_visited[coordinate_row[sub_col]][sub_col]:
                            q.put((coordinate_row[sub_col], sub_col))
                            queue_visited[coordinate_row[sub_col]][sub_col] = True
                        visited[cur_row][sub_col] = True
                        coordinate_row[sub_col] = cur_row
                        break

        x = 10e10
        for col, row in coordinate_row.items():
            x = min(x, B[row][col])

        small_list[0] = x
        for col, row in coordinate_row.items():
            B[row][col] -= x
            small_list[row+1] = col + 1
        big_list.append(small_list)
        print(small_list)
    if count == 2500 and B != [[0] * n] * n:
        print(-1)
        return
    else:
        print(len(big_list))
        for i in range(len(big_list)):
            print(*big_list[i])

tc = int(input())
for _ in range(tc):
    n = int(input())
    B = []
    for _ in range(n):
        B.append(list(map(int, input().split())))
    main(B)

#
# 1
# 6
# 459315640 459315640 459315640 459315640 459315640 459315640
# 459315640 459315640 459315640 459315640 459315640 459315640
# 459315640 459315640 459315640 459315640 459315640 459315640
# 459315640 459315640 459315640 459315640 459315640 459315640
# 459315640 459315640 459315640 459315640 459315640 459315640
# 459315640 459315640 459315640 459315640 459315640 459315640
