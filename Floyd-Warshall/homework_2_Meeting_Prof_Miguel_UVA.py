while True:
    num_path = int(input())
    if num_path == 0:
        break
    list_path = []
    vertex_set = set()
    vertex_dic = {}

    for _ in range(num_path):
        road = list(input().split())
        vertex_1 = ord(road[2]) - ord('A')
        vertex_2 = ord(road[3]) - ord('A')
        vertex_set.add(vertex_1)
        vertex_set.add(vertex_2)
        list_path.append(road)
    young_location, old_location = input().split()
    vertex_set.add(ord(young_location) - ord('A'))
    vertex_set.add(ord(old_location) - ord('A'))
    num_vertex = max(vertex_set) + 1

    for vertex in range(num_vertex):
        vertex_dic[chr(vertex + ord('A'))] = vertex

    young_location, old_location = vertex_dic[young_location], vertex_dic[old_location]
    dist_young = [[10e9]*num_vertex for _ in range(num_vertex)]
    dist_old = [[10e9]*num_vertex for _ in range(num_vertex)]
    # print(vertex_set)
    # print(num_vertex)
    for some_path in list_path:
        if some_path[0] == 'Y':
            if some_path[1] == 'U':
                dist_young[vertex_dic[some_path[2]]][vertex_dic[some_path[3]]] = min(int(some_path[4]),dist_young[vertex_dic[some_path[2]]][vertex_dic[some_path[3]]])
            elif some_path[1] == 'B':
                dist_young[vertex_dic[some_path[2]]][vertex_dic[some_path[3]]] = min(int(some_path[4]),dist_young[vertex_dic[some_path[2]]][vertex_dic[some_path[3]]])
                dist_young[vertex_dic[some_path[3]]][vertex_dic[some_path[2]]] = min(int(some_path[4]),dist_young[vertex_dic[some_path[3]]][vertex_dic[some_path[2]]])
        elif some_path[0] == 'M':
            if some_path[1] == 'U':
                dist_old[vertex_dic[some_path[2]]][vertex_dic[some_path[3]]] = min(int(some_path[4]),dist_old[vertex_dic[some_path[2]]][vertex_dic[some_path[3]]])
            elif some_path[1] == 'B':
                dist_old[vertex_dic[some_path[2]]][vertex_dic[some_path[3]]] = min(int(some_path[4]),dist_old[vertex_dic[some_path[2]]][vertex_dic[some_path[3]]])
                dist_old[vertex_dic[some_path[3]]][vertex_dic[some_path[2]]] = min(int(some_path[4]),dist_old[vertex_dic[some_path[3]]][vertex_dic[some_path[2]]])
    # print(vertex_dic)
    # print(dist_young)
    # print(dist_old)
    for i in range(num_vertex):
        for j in range(num_vertex):
            if i == j:
                dist_young[i][j] = 0
                dist_old[i][j] = 0


    for k in range(num_vertex):
        for i in range(num_vertex):
            for j in range(num_vertex):
                if dist_young[i][k] == 10e9:
                    pass
                else:
                    if dist_young[k][j] != 10e9 and dist_young[i][k] + dist_young[k][j] < dist_young[i][j]:
                        dist_young[i][j] = dist_young[i][k] + dist_young[k][j]

                if dist_old[i][k] == 10e9:
                    pass
                else:
                    if dist_old[k][j] != 10e9 and dist_old[i][k] + dist_old[k][j] <= dist_old[i][j]:
                        dist_old[i][j] = dist_old[i][k] + dist_old[k][j]

    # print(dist_young)
    # print(dist_old)
    real_dist = 10e9
    middle_location = []
    for i in range(num_vertex):
        if dist_young[young_location][i] + dist_old[old_location][i] < real_dist:
            real_dist = dist_young[young_location][i] + dist_old[old_location][i]
            middle_location.clear()
            middle_location.append(i)
        elif dist_young[young_location][i] + dist_old[old_location][i] == real_dist:
            middle_location.append(i)

    middle_location = sorted(middle_location)
    middle_location = [chr(ord('A') +i) for i in middle_location]
    if real_dist == 10e9:
        print('You will never meet.')
    else:
        print(real_dist, *middle_location)