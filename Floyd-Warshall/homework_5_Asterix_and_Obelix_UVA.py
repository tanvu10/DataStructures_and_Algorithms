from copy import deepcopy


def floyd_warshall_with_party(dist, num_vertex, party_cost):
    original_dist = deepcopy(dist)
    for _ in range(2):
        for k in range(num_vertex):
            for i in range(num_vertex):
                for j in range(num_vertex):
                    if dist[i][k] == 10e9:
                        continue
                    max_party_cost = max(party_cost[i][k], party_cost[k][j])
                    if dist[k][j] != 10e9 and dist[i][k] + dist[k][j] + max_party_cost < dist[i][j] + party_cost[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        party_cost[i][j] = max_party_cost

    return dist


count = 1
while True:
    num_city, num_path, num_query = map(int, input().split())
    if num_city == num_path == num_query == 0:
        break
    list_cost = list(map(int, input().split()))
    dist = [[10e9]*num_city for _ in range(num_city)]

    party_cost = [[10e9]*num_city for _ in range(num_city)]

    for _ in range(num_path):
        start, stop, cost = map(int, input().split())
        dist[start-1][stop-1] = cost
        dist[stop-1][start-1] = cost


    for i in range(num_city):
        for j in range(num_city):
            if i == j:
                party_cost[i][j] = list_cost[i]
            else:
                party_cost[i][j] = max(list_cost[i], list_cost[j])
                party_cost[j][i] = max(list_cost[i], list_cost[j])


    queries_list = []
    dist = floyd_warshall_with_party(dist, num_city, party_cost)
    # print(dist)
    print(f'Case #{count}')
    for _ in range(num_query):
        start, stop = map(int, input().split())
        queries_list.append((start,stop))
        if dist[start-1][stop-1] == 10e9:
            print(-1)
        else:
            print(dist[start-1][stop-1] + party_cost[start-1][stop-1])
    print()
    count+=1