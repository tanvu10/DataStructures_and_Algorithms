import heapq

num_tc = int(input())
for _ in range(num_tc):
    cost = int(input())
    num_building = int(input())
    num_path = int(input())
    graph = [[] for _ in range(num_building+1)]
    for _ in range(num_path):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    visited = [False]*(num_building+1)
    dist = [10e9]*(num_building+1)

    sta = 1
    dist[sta] = 0
    heap = []
    heapq.heappush(heap, (dist[sta], sta))
    while len(heap) > 0:
        cur_dis, cur_des = heapq.heappop(heap)
        if visited[cur_des]:
            continue
        visited[cur_des] = True
        for next_des, next_dis in graph[cur_des]:
            if not visited[next_des] and next_dis < dist[next_des]:
                dist[next_des] = next_dis
                heapq.heappush(heap, (dist[next_des], next_des))
    print(sum(dist[1:])*cost)