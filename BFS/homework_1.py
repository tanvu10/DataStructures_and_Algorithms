truy_van = int(input())
input_path_list = []
i= 0
E_V_list = []
start_list = []
while i < truy_van:
    E_V = list(input().split(' '))
    E_V_list.append(int(E_V[0]))
    # print(E_V[1])
    sub_list= []
    for _ in range(int(E_V[1])):
        node = list(input().split(' '))
        sub_list.append(node)
    input_path_list.append(sub_list)
    start = int(input())
    start_list.append(start)
    i += 1

# print(input_path_list)
# print(E_V_list)
# print(start_list)

from queue import Queue
def BFS(vertex, path_list, start):
    length = 6
    graph = [[] for i in range(vertex+1)]
    track_visited = [False for i in range(vertex+1)]
    # track_path = [-1 for i in range(vertex+1)]
    track_dist = [-1 for i in range(vertex+1)]
    #store in graph
    for sub_list in path_list:
        graph[int(sub_list[0])].append(int(sub_list[1]))
        graph[int(sub_list[1])].append(int(sub_list[0]))
    track_dist[start] = 0
    track_visited[start] = True
    q = Queue()
    q.put(start)

    while not q.empty():
        current_vertex = q.get()
        for near_vertex in graph[current_vertex]:
            if track_visited[near_vertex] == False:
                #neu chua visiter thi` moi dua vao hang cho`
                track_visited[near_vertex] = True
                track_dist[near_vertex] = track_dist[current_vertex] + 1
                q.put(near_vertex)
            else:
                pass

    new_dis = [0]*(len(track_dist))
    for i in range(len(track_dist)):
        if track_dist[i] >= 0:
            new_dis[i] = track_dist[i]*6
        else:
            new_dis[i] = track_dist[i]

    new_dis.pop(start)
    new_dis.pop(0)
    # print('start',start)

    # print('graph',graph)
    # print('track path',track_path)
    # print('track visited', track_visited)
    # print(path_list)
    # print('track dis', track_dist)
    # print('new dis',new_dis)

    print(str(new_dis).replace(',','')[1:-1])


for num in range(truy_van):
    BFS(E_V_list[num], path_list= input_path_list[num], start = start_list[num] )













