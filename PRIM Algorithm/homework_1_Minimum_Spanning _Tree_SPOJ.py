import heapq

num_node, num_edge = map(int, input().split())
graph = [[] for _ in range(num_node+1)]
for _ in range(num_edge):
    sta, sto, cost = map(int, input().split())
    graph[sta].append((sto, cost))
    graph[sto].append((sta, cost))

visited = [False]*(num_node+1)
dist = [10e9]*(num_node+1)
heap = []
start = 1
dist[0] = 0
# visited[start] = True
dist[start] = 0
heapq.heappush(heap, (dist[start], start))

while len(heap) > 0:
    current_cost, current_point = heapq.heappop(heap)
    if visited[current_point]:
        continue
    visited[current_point] = True
    for next_point, next_cost in graph[current_point]:
        if not visited[next_point] and next_cost < dist[next_point]:
            dist[next_point] = next_cost
            heapq.heappush(heap, (dist[next_point], next_point))

# print((dist))
total_weight = sum(dist)
print(total_weight)