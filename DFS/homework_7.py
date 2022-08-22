dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 0, 1, -1, 0, 1, -1]

while True:
    row, col = map(int, input().split())
    if row == 0 and col == 0:
        break
    else:
        graph = []
        for _ in range(row):
            graph.append(list(input()))
        print(graph)
        visited = [[False]*col for _ in range(row)]


        def DFS(graph, r, c, visited, num_track):
            #base case:
            global count
            count +=1
            visited[r][c] = True
            for i in range(len(dr)):
                new_r = r + dr[i]
                new_c = c + dc[i]
                if 0 <= new_r < row and  0 <= new_c < col and visited[new_r][new_c] == False and ord(graph[new_r][new_c]) == num_track:
                    DFS(graph, r, c, visited, ord(graph[new_r][new_c]))
            visited[r][c] = False
            return num_track




        max_length = 0
        for r in range(row):
            for c in range(col):
                if not visited[r][c] and ord(graph[r][c]) == 65:
                    count = 0
                    ans = DFS(graph, r, c, visited, ord(graph[r][c]) + 1 )
                    if count > max_length:
                        max_length = count

