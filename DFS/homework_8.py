num_case = int(input())
for _ in range(num_case):
    num_location = int(input())
    # print(num_location)
    graph = [[] for _ in range(num_location+1)]
    # len_matrix = [[0]*(num_location+1) for _ in range(num_location+1)]
    len_dic = {}
    for _ in range(num_location - 1):
        start, end, length = map(int, input().split())
        # print(start, end)
        # print(start, end)
        graph[start].append((end, length))
        graph[end].append((start, length))
        # len_matrix[start][end] = length
        # len_matrix[end][start] = length
        # len_dic[str(start) + str(end)] = length

    # print(len_dic)
    start = 1
    max_length = 0
    for _ in range(2):
        current_max = 0
        dis_list = [0]*(num_location+1)
        stack = []
        stack.append(start)
        visited = [False]*(num_location+1)
        visited[start] = True
        while len(stack) > 0:
            current_node = stack.pop()
            for next_node, leng in graph[current_node]:
                if not visited[next_node]:
                    stack.append(next_node)
                    visited[next_node] = True
                    # if (str(next_node) + str(current_node)) in len_dic.keys():
                    #     dis_list[next_node] = dis_list[current_node] + len_matrix[next_node][current_node]
                    dis_list[next_node] = dis_list[current_node] + leng
                    if dis_list[next_node] >= current_max:
                        current_max = dis_list[next_node]

        max_length = current_max
        start = dis_list.index(max_length)
    print(max_length)
