import heapq
def prim(num_des, sta):
    global graph
    global MSTgraph
    global visited
    dist = [10e9]*(num_des+1)
    dist[sta] = 0
    heap = []
    path = [-1]*(num_des+1)
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
                path[next_des] = cur_des

    for des in range(1, num_des+1):
        if path[des] != -1:
            pre_des, cost = path[des], dist[des]
            MSTgraph[pre_des].append((des, cost))
            MSTgraph[des].append((pre_des, cost))
    # print(visited)
    # print(path)
    # print(MSTgraph)

def dfs(sta, sto, level):
    global visited
    global MSTgraph
    visited[sta] = True
    if sta == sto:
        return level
    for next_des, next_cost in MSTgraph[sta]:
        if not visited[next_des]:
            tmp_level = dfs(next_des, sto, max(level, next_cost))
            if tmp_level != 10e9:
                return tmp_level
    return 10e9

case = 1
while True:
    num_des, num_path, num_q = map(int, input().split())
    if num_des == num_q == num_path == 0:
        break
    graph = [[] for _ in range(num_des+1)]
    MSTgraph = [[] for _ in range(num_des+1)]
    for _ in range(num_path):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    visited = [False]*(num_des+1)
    for u in range(1, num_des+1):
        if not visited[u]:
            prim(num_des, u)

    print(f'Case #{case}')
    for _ in range(num_q):
        visited = [False] * (num_des + 1)
        sta, sto = map(int, input().split())
        dis = dfs(sta, sto, 0)
        if dis == 10e9:
            print('no path')
        else:
            print(dis)
    case += 1
    print()