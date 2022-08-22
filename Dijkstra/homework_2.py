import heapq
num_vertex = int(input())
graph = [[] for _ in range(num_vertex+1)]
destination = int(input())
time_constraint = int(input())
num_path = int(input())
for _ in range(num_path):
    a, b, time = map(int, input().split())
    graph[a].append((b, time))

count_mouse = 0
for start in range(1,num_vertex+1):
    start_point = start
    graph_heap = []
    dist = [10e9]*(num_vertex+1)
    dist[start_point] = 0
    heapq.heappush(graph_heap, (0, start_point))
    while len(graph_heap) > 0:
        current_weight, current_point = heapq.heappop(graph_heap)
        if dist[current_point] != current_weight:
            continue
        for next_point, next_weight in graph[current_point]:
            if dist[current_point] + next_weight < dist[next_point]:
                dist[next_point] = dist[current_point] + next_weight
                heapq.heappush(graph_heap, (dist[next_point], next_point))
    # print('start',start_point)
    # print('stop',destination)
    # print(dist)
    if dist[destination] <= time_constraint:
        count_mouse+=1

print(count_mouse)
