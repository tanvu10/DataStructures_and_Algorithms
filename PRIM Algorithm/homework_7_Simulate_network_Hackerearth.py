import heapq

num_comp, num_cable = map(int, input().split())
graph = [[] for _ in range(num_comp+1)]
for _ in range(num_cable):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

visited = [False]*(num_comp+1)
dist = [10e9]*(num_comp+1)
heap = []
start = 1
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


new_dist = sorted(dist[1:], reverse=True)
num_replace_cable = int(input())
replace_cable_list = list(map(int, input().split()))
replace_cable_list = sorted(replace_cable_list)

for i in range(min(len(new_dist), len(replace_cable_list))):
    if new_dist[i] > replace_cable_list[i]:
        new_dist[i], replace_cable_list[i] = replace_cable_list[i], new_dist[i]
    else:
        break
print(sum(new_dist))

