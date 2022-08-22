num_country = int(input())
graph = [[] for _ in range(num_country+1)]
for _ in range(num_country-1):
    start, stop = map(int, input().split(' '))
    graph[start].append(stop)
    graph[stop].append(start)

# print(graph)
num_girl = int(input())
girl_list = [False]*(num_country+1)
for _ in range(num_girl):
    index = int(input())
    girl_list[index] = True
# print(girl_list)

visited = [False]*(num_country+1)
track_path = [-1]*(num_country+1)
stack = []
start = 1
stack.append(start)
visited[start] = True
distance_list = [0]*(num_country+1)

while len(stack) > 0:
    current_node = stack.pop()
    for next_node in graph[current_node]:
        if not visited[next_node]:
            stack.append(next_node)
            visited[next_node] = True
            # track_path[next_node] = current_node
            distance_list[next_node] = distance_list[current_node] +1

# print(visited)
# print([j for j in range(len(track_path))])
# print(distance_list)

# girl_min = min(distance_list
girl_min = min([distance_list[i] for i in range(len(distance_list)) if distance_list[i] > 0 and girl_list[i] == True])
index = []
for i in range(len(girl_list)):
    if distance_list[i] == girl_min and girl_list[i] == True:
        index.append(i)


print(min(index))
# print(girl_min)

#
# distance_count = []
# for girl_index in range(len(girl_list)):
#     if girl_list[girl_index]