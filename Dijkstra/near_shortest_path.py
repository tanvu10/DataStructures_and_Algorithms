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

while True:
    num_vertex, num_path = map(int, input().split())
    if num_vertex == 0 and num_path == 0:
        break
    begin, end = map(int, input().split())
    graph_from_begin = [[] for _ in range(num_vertex)]
    graph_to_end = [[] for _ in range(num_vertex)]
    for _ in range(num_path):
        sta, sto, cost = map(int, input().split())
        graph_from_begin[sta].append((sto, cost))
        graph_to_end[sto].append((sta,cost))
    dist_from_begin = Dijsktra(begin, graph_from_begin, num_vertex)
    dist_to_end = Dijsktra(end, graph_to_end, num_vertex)
    # save shortest path length
    shortest_length = dist_from_begin[end]
    near_shortest_path_list = [[] for _ in range(num_vertex)]

    for start_point in range(len(graph_from_begin)):
        for next_point, cost in graph_from_begin[start_point]:
            if dist_from_begin[start_point] + cost + dist_to_end[next_point] != shortest_length:
                near_shortest_path_list[start_point].append((next_point, cost))

    dist_near_shortest_path = Dijsktra(begin,near_shortest_path_list, num_vertex )
    if dist_near_shortest_path[end] == 10e9:
        print(-1)
    else:
        print(dist_near_shortest_path[end])
