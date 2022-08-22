import heapq
from math import sqrt
while True:
    try:
        num_bulding = int(input())
        list_building = []
        for _ in range(num_bulding):
            x, y = map(int, input().split())
            list_building.append((x, y))

        graph = [[] for _ in range(num_bulding+1)]
        for i in range(len(list_building)):
            for j in range(len(list_building)):
                sta = i+1
                sto = j+1
                x_sta, y_sta = list_building[i]
                x_sto, y_sto = list_building[j]
                dis = sqrt((x_sta-x_sto)**2 + (y_sta-y_sto)**2)
                graph[sta].append((sto, dis))
        # print(graph)
        init = 1
        visit = [False]*(num_bulding+1)
        dist = [10e9]*(num_bulding+1)
        path = [-1]*(num_bulding+1)
        dist[init] = 0
        h = []
        heapq.heappush(h, (dist[init], init))

        # print(dist)
        # print(path)
        num_cable = int(input())
        for _ in range(num_cable):
            a, b = map(int, input().split())
            graph[a][b-1] = (b, 0)
            graph[b][a-1] = (a, 0)
        while len(h) > 0:
            cur_dist, cur_des = heapq.heappop(h)
            if visit[cur_des] == True:
                continue
            visit[cur_des] = True
            for next_des, next_dist in graph[cur_des]:
                if not visit[next_des] and next_dist < dist[next_des]:
                    dist[next_des] = next_dist
                    path[next_des] = cur_des
                    heapq.heappush(h, (dist[next_des], next_des))

        print("%.2f" % sum(dist[1:]))
    except EOFError:
        break
