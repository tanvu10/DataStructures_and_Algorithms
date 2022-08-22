import heapq

def Dijsktra(begin, graph, num_vertex):
    heap = []
    dist = [10e9] * (num_vertex + 1)
    dist[begin] = 0
    heapq.heappush(heap, (dist[begin], begin))
    while len(heap) > 0:
        current_weight, current_point = heapq.heappop(heap)
        if current_weight != dist[current_point]:
            continue
        for next_point, next_weight in graph[current_point]:
            if dist[current_point] + next_weight < dist[next_point]:
                dist[next_point] = dist[current_point] + next_weight
                heapq.heappush(heap, (dist[next_point], next_point))
    return dist

num_testcase = int(input())
for case in range(num_testcase):
    num_building = int(input())
    num_path = int(input())
    list_path = []
    graph = [[] for _ in range(num_building+1)]

    for _ in range(num_path):
        sta, sto = map(int, input().split())
        graph[sta].append((sto,1))
        graph[sto].append((sta,1))
    begin, end = map(int,input().split())


    from_begin_dist = Dijsktra(begin, graph, num_building)
    to_end_dist = Dijsktra(end, graph, num_building)
    # print(from_begin_dist)
    # print(to_end_dist)
    total_time = 0
    for i in range(len(from_begin_dist)):
        if from_begin_dist[i] != 10e9:
            total_time = max(total_time,from_begin_dist[i] + to_end_dist[i])
    print(f'Case {case+1}: {total_time}')


