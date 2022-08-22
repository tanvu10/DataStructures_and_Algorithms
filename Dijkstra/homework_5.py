import heapq
num_testcase = int(input())
for case in range(num_testcase):
    N_sever, M_cable, begin, end = map(int, input().split())
    graph = [[] for _ in range(N_sever)]
    for _ in range(M_cable):
        start, stop, time = map(int, input().split())
        graph[start].append((stop, time))
        graph[stop].append((start,time))

    heap = []
    dist = [10e9]*(N_sever)
    dist[begin] = 0
    heapq.heappush(heap,(dist[begin], begin))
    while len(heap) > 0:
        current_time, current_point = heapq.heappop(heap)
        if dist[current_point] != current_time:
            continue
        for next_point, next_time in graph[current_point]:
            if dist[current_point] + next_time < dist[next_point]:
                dist[next_point] = dist[current_point] + next_time
                heapq.heappush(heap, (dist[next_point], next_point))

    if dist[end] == 10e9:
        print(f'Case #{case + 1}: unreachable')
    else:
        print(f'Case #{case + 1}: {dist[end]}')