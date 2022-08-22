num_bomb, num_connection = map(int, input().split())
graph = [[] for _ in range(num_bomb+1)]
for _ in range(num_connection):
    start, end = map(int, input().split())
    # print(start, end)
    # print(start, end)
    graph[start].append(end)


def bug_(graph):
    max_count = 0
    for i in range(1, num_bomb+1):
        visited = [False] * (num_bomb + 1)
        count = 0
        if not visited[i]:
            stack = []
            stack.append(i)
            visited[i] = True
            while len(stack) >0:
                count += 1
                current_node = stack.pop()
                for next_node in graph[current_node]:
                    if not visited[next_node]:
                        stack.append(next_node)
                        visited[next_node] = True
        if count >= max_count:
            max_count = count
    print(max_count)

bug_(graph)