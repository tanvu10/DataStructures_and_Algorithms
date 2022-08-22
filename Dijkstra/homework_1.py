import heapq
num_road = int(input())
graph = [[] for _ in range(500+1)]
dist = [10**9 for _ in range(500+1) ]
for _ in range(num_road):
    A, B, weight = map(int, input().split())
    graph[A].append((B, weight))
    graph[B].append((A, weight))

start_point = int(input())
num_stop = int(input())
stop_list = []
for _ in range(num_stop):
    stop_list.append(int(input()))

graph_heap = []
heapq.heappush(graph_heap, (0,start_point))
dist[start_point] = 0
while len(graph_heap) > 0:
    current_weight, current_point  = heapq.heappop(graph_heap)
    if current_weight > dist[current_point]:
        continue
    for next_point, next_weight  in graph[current_point]:
        if current_weight + next_weight < dist[next_point]:
            dist[next_point] = current_weight + next_weight
            heapq.heappush(graph_heap, ( dist[next_point],next_point))


for destination in stop_list:
    if dist[destination] == 10**9:
        print('NO PATH')
    else:
        print(dist[destination])