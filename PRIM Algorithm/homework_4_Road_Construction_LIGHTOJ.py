import heapq
num_tc = int(input())
for time in range(num_tc):
    input()
    num_path = int(input())
    path_list = list()
    name_set = set()
    for _ in range(num_path):
        a, b, c = input().split()
        name_set.add(a)
        name_set.add(b)
        path_list.append((a, b, c))
    name_to_number_dic = {}
    number_to_name_dic = {}

    name_set = list(name_set)
    for i in range(len(name_set)):
        name_to_number_dic[name_set[i]] = i
        number_to_name_dic[i] = name_set

    graph = [[] for _ in range(len(name_set))]
    for a, b, c in path_list:
        sta = name_to_number_dic[a]
        sto = name_to_number_dic[b]
        graph[sta].append((sto, int(c)))
        graph[sto].append((sta, int(c)))

    visited = [False]*(len(name_set))
    dist = [10e9]*(len(name_set))

    sta = 0
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

    if sum(dist) < 10e9:
        print(f'Case {time+1}: {sum(dist)}')
    else:
        print(f'Case {time+1}: Impossible')
