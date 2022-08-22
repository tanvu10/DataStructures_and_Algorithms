import heapq
num_node, num_edge = map(int, input().split())
graph = [[] for _ in range(num_node+1)]
for _ in range(num_edge):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

visited = [False]*(num_node+1)
dist = [10e9]*(num_node+1)
heap = []
start = int(input())
dist[start] = 0
heapq.heappush(heap,(dist[start], start))
while len(heap) > 0:
    current_cost, current_des = heapq.heappop(heap)
    if visited[current_des]:
        continue
    visited[current_des] = True
    for next_des, next_cost in graph[current_des]:
        if not visited[next_des] and next_cost < dist[next_des]:
            dist[next_des] = next_cost
            heapq.heappush(heap, (dist[next_des], next_des))

sum_dist = 0
for i in range(len(dist)):
    if dist[i] != 10e9:
        sum_dist += dist[i]
print(sum_dist)
