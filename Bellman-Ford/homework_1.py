num_case = int(input())
for _ in range(num_case):
    star, worm_hole = map(int,input().split())
    graph = [[] for _ in range(star)]
    for _ in range(worm_hole):
        sta, sto, cost = map(int,input().split())
        graph[sta].append((sto, cost))


    dist = [10e9]*star
    dist[0] = 0
    for _ in range(star):
        for current_point in range(len(graph)):
            for next_point, cost in graph[current_point]:
                if dist[current_point] != 10e9 and dist[current_point] + cost < dist[next_point]:
                    dist[next_point] = dist[current_point] + cost

    check = False
    for current_point in range(len(graph)):
        for next_point, cost in graph[current_point]:
            if dist[current_point] != 10e9 and dist[current_point] + cost < dist[next_point]:
                check = True
    if check:
        print('possible')
    else:
        print('not possible')
