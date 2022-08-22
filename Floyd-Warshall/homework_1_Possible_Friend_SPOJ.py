num_testcase = int(input())
for _ in range(num_testcase):
    some_matrix = []
    first_line = list(input())
    some_matrix.append(first_line)
    for _ in range(len(first_line)-1):
        some_line = list(input())
        some_matrix.append(some_line)
    dist = [[10e9]*(len(some_matrix)) for _ in range(len(some_matrix))]
    # print(dist)
    for i in range(len(some_matrix)):
        for j in range(len(some_matrix)):
            if i == j:
                dist[i][j] = 0
            else:
                if some_matrix[i][j] == 'Y':
                    dist[i][j] = 1
    # print(dist)
    for k in range(len(some_matrix)):
        for i in range(len(some_matrix)):
            for j in range(len(some_matrix)):
                if dist[i][k] == 10e9:
                    continue
                if dist[k][j] != 10e9 and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    friend_index = 0
    max_friend = 0
    for i in range(len(some_matrix)):
        current_max_friend = 0
        for j in range(len(some_matrix)):
            if dist[i][j] == 2 :
                current_max_friend += 1
        if current_max_friend > max_friend:
            friend_index = i
            max_friend = current_max_friend
    print(friend_index, max_friend)