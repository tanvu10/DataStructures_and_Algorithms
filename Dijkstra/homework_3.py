import heapq
constraint_cost = 200000
num_testcase = int(input())
for _ in range(num_testcase):
    num_city = int(input())
    dic_map = {}
    graph = [[] for _ in range(num_city+1)]
    for city_num in range(1,num_city+1):
        city_name = input()
        dic_map[city_name] = city_num
        num_road = int(input())
        for _ in range(num_road):
            next_city, cost = map(int, input().split())
            graph[city_num].append((next_city, cost))

    num_case = int(input())
    for _ in range(num_case):
        start, destination = input().split()
        heap = []
        dist = [10e9]*(num_city+1)
        start_city = dic_map[start]
        end_city = dic_map[destination]
        dist[start_city] = 0
        heapq.heappush(heap, (dist[start_city], start_city))
        while len(heap) > 0:
            current_cost, current_city = heapq.heappop(heap)
            if dist[current_city] != current_cost:
                continue
            for next_city, next_cost in graph[current_city]:
                if dist[current_city] + next_cost < dist[next_city]:
                    dist[next_city] = dist[current_city] + next_cost
                    heapq.heappush(heap,(dist[next_city], next_city))
        print(dist[end_city])
    input()