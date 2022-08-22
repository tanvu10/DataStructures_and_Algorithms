T = int(input())
name = 'ALLIZZWELL'
# print(name[1])

dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 0, 1, -1, 0, 1, -1]
def DFS(graph, r,c,length, visited_matrix):
    if length == len(name):
        return True
    visited_matrix[r][c] = True
    for i in range(len(dr)):
        new_r = r + dr[i]
        new_c = c + dc[i]
        if 0 <= new_r < R and  0 <= new_c < C and visited_matrix[new_r][new_c] == False and graph[new_r][new_c] == name[length]:
            # visited_matrix[new_r][new_c] = True
            if DFS(graph, new_r, new_c, length + 1, visited_matrix):
                return True
    visited_matrix[r][c] = False
    return False


for _ in range(T):
    R, C = map(int, input().split())
    graph = []
    # check_matrix = [[False]*C for _ in range(R)]
    for i in range(R):
        graph.append(list(input()))
    # print(graph)

    def bug(graph, C, R):
        visited_matrix = [[False]*C for _ in range(R)]
        # answer = 'NO'
        for r in range(R):
            for c in range(C):
                if graph[r][c] == 'A' and not visited_matrix[r][c]:
                    length = 0
                    ans = DFS(graph, r, c, length + 1, visited_matrix)
                    if ans:
                        return print('YES')
        return print('NO')
    bug(graph, C, R)
    input()