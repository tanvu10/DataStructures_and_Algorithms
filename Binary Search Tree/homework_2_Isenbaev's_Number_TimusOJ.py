from queue import Queue
num_team = int(input())
location = 0
location_dic = {}
inverse_location_dic = {}
team_list = []

for _ in range(num_team):
    name1, name2, name3 = input().split()
    # print(name1, name2, name3)
    team_list.append((name1, name2, name3))
    if name1 not in location_dic.keys():
        location_dic[name1] = location
        inverse_location_dic[location] = name1
        location += 1
    if name2 not in location_dic.keys():
        location_dic[name2] = location
        inverse_location_dic[location] = name2
        location += 1
    if name3 not in location_dic.keys():
        location_dic[name3] = location
        inverse_location_dic[location] = name3
        location += 1

visited = [False]*len(location_dic.keys())
graph = [[] for _ in range(len(location_dic.keys()))]
dist = [10e9]*len(location_dic.keys())
for name1, name2, name3 in team_list:
    graph[location_dic[name1]].append(location_dic[name2])
    graph[location_dic[name1]].append(location_dic[name3])
    graph[location_dic[name2]].append(location_dic[name1])
    graph[location_dic[name2]].append(location_dic[name3])
    graph[location_dic[name3]].append(location_dic[name2])
    graph[location_dic[name3]].append(location_dic[name1])
def BFS(graph):
    start = 'Isenbaev'
    if start not in location_dic.keys():
        for key in sorted(location_dic.keys()):
            print(key, 'undefined')
        return
    else:
        start_index = location_dic[start]
        dist[start_index] = 0
        visited[start_index] = True

        q = Queue()
        q.put(start_index)

        while not q.empty():
            current = q.get()
            for next in graph[current]:
                if not visited[next]:
                    dist[next] = dist[current] + 1
                    visited[next] = True
                    q.put(next)

        new_location_dic = {}
        for i in range(len(dist)):
            new_location_dic[inverse_location_dic[i]] = dist[i]

        for key in sorted(new_location_dic.keys()):
            if new_location_dic[key] == 10e9:
                print(key, 'undefined')
            else:
                print(key, new_location_dic[key])

BFS(graph)
# print(location_dic)