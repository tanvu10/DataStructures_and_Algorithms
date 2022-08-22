import heapq
num_tc = int(input())

def prim(source):
    global graph
    global num_school
    visited = [False]*(num_school+1)
    dist = [10e9]*(num_school+1)
    dist[source] = 0
    heap = []
    heapq.heappush(heap, (dist[source], source))
    trace = [{} for _ in range(num_school+1)]
    while len(heap) > 0:
        cur_dis, cur_des = heapq.heappop(heap)
        if visited[cur_des]:
            continue
        visited[cur_des] = True

        for i in range(len(graph[cur_des])):
            next_des, next_dis = graph[cur_des][i]
            if not visited[next_des] and next_dis < dist[next_des]:
                dist[next_des] = next_dis
                heapq.heappush(heap, (dist[next_des], next_des))
                trace[next_des] = {'path': cur_des, 'index': i}
    # print(trace)
    sum_ = sum(dist[1:])
    return sum_, trace


for _ in range(num_tc):
    num_school, num_connection = map(int, input().split())
    graph = [[] for _ in range(num_school+1)]
    for _ in range(num_connection):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    min_list = []
    min_one, track = prim(1)
    min_two = 10e9
    for i in range(2, num_school+1):
        sub_track = track[i]
        pre_des = sub_track['path']
        index = sub_track['index']
        # graph[pre_dex][index]: way from pre_des ==>> i
        next_des, next_cost = graph[pre_des][index]
        tmp_cost = next_cost
        temp_des = next_des
        graph[pre_des][index] = (temp_des, 10e9)
        new_min, tmp_track = prim(1)
        min_two = min(min_two, new_min)
        graph[pre_des][index] = (temp_des, tmp_cost)

    print(min_one, min_two)