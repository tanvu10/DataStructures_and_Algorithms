import heapq

num_testcase = int(input())
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

for _ in range(num_testcase):
    num_vertex, num_oneway, num_twoway, begin, destination  = map(int, input().split())
    from_begin_graph = [[] for _ in range(num_vertex+1)]
    to_end_graph = [[] for _ in range(num_vertex+1)]
    two_way_list = []
    for _ in range(num_oneway):
        start, stop , cost = map(int, input().split())
        from_begin_graph[start].append((stop, cost))
        to_end_graph[stop].append((start, cost))
    for _ in range(num_twoway):
        start, stop , cost = map(int, input().split())
        two_way_list.append((start, stop , cost))

    dist_from_begin = Dijsktra(begin, from_begin_graph, num_vertex)
    dist_to_end = Dijsktra(destination, to_end_graph, num_vertex)

    min_cost = 10e9
    for sta, sto, co in two_way_list:
        # graph[sta].append((sto, co))
        some_graph = min(dist_from_begin[sta] + co + dist_to_end[sto], dist_from_begin[sto] + co + dist_to_end[sta] )
        min_cost = min(min_cost, some_graph)

    if min_cost == 10e9:
        print(-1)
    else:
        print(min_cost)