import sys
sys.setrecursionlimit(10000)
test_case = int(input())
for _ in range(test_case):
    num_doc, num_connection = map(int, input().split(' '))
    graph = [[] for _ in range(num_doc+1)]
    for _ in range(num_connection):
        start, end = map(int, input().split(' '))
        # print(start, end)
        graph[start].append(end)
        # graph[end].append(start)
    def DFS(start_point, visited, check, graph):
        visited[start_point] = True
        check[start_point] = True
        for next_point in graph[start_point]:
            if not visited[next_point]:
                answer = DFS(next_point, visited, check, graph)
                if answer == True:
                    return True
            elif check[next_point] == True:
                return True
        check[start_point] = False
        return False

    def bug_(graph, num_doc):
        visited_doc = [False] * (num_doc + 1)
        cycle_check = [False] * (num_doc + 1)
        for i in range(1, num_doc+1):
            if visited_doc[i] == False:
                if DFS(i, visited_doc, cycle_check, graph):
                    return print('YES')
        return print('NO')
    bug_(graph, num_doc)