import math
import heapq
num_tc = int(input())
for _ in range(num_tc):
    input()
    num_tn = int(input())
    list_location = []
    for _ in range(num_tn):
        x, y = map(float, input().split())
        list_location.append((x,y))
    graph = [[] for _ in range(num_tn)]
    for i in range(len(list_location)):
        for j in range(len(list_location)):
            x_sta, y_sta = list_location[i]
            x_sto, y_sto = list_location[j]
            distance = math.sqrt((x_sta-x_sto)**2 + (y_sta-y_sto)**2)
            graph[i].append((j, distance))
    print(graph)

    heap = []
    start = 0
    dist = [10e9]*num_tn
    dist[start] = 0
    visit = [False]*num_tn
    heapq.heappush(heap, (dist[start], start))
    while len(heap) > 0:
        cur_cost, cur_des  = heapq.heappop(heap)
        if visit[cur_des]:
            continue
        visit[cur_des] = True
        for next_des, next_cost in graph[cur_des]:
            if not visit[next_des] and next_cost < dist[next_des]:
                dist[next_des] = next_cost
                heapq.heappush(heap, (dist[next_des], next_des))
    print("%.2f" % sum(dist))
    print()
