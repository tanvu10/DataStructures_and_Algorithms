from queue import Queue

features = list(input().split(' '))
num_edge = int(features[0])
max_cat = int(features[1])

cat_edge = list(input().split(' '))
list_cat = [0]
[list_cat.append(int(cat)) for cat in cat_edge]
# print(list_cat)
i = 0
graph = [[] for _ in range(num_edge + 1)]
visited = [0 for _ in range(num_edge + 1)]
cat_count_check = [0 for _ in range(num_edge + 1)]

while i < num_edge - 1:
    start, stop = (input().split(' '))
    graph[int(start)].append(int(stop))
    graph[int(stop)].append(int(start))
    i += 1

# print(graph)

child_note = 1
visited[child_note] = 1
if list_cat[child_note] == 1:
    cat_count_check[child_note] = 1
else:
    pass

q = Queue()
q.put(child_note)
num_res = []
while not q.empty():
    current_node = q.get()
    count = 0
    if len(graph[current_node]) > 0:
        for next_node in graph[current_node]:
            # check if visited:
            if visited[next_node] == 0:
                if list_cat[current_node] == 1:
                    cat_count_check[next_node] = cat_count_check[current_node] + list_cat[next_node]
                else:
                    cat_count_check[next_node] = list_cat[next_node]
                # print(cat_count_check)
                if cat_count_check[next_node] <= max_cat:
                    q.put(next_node)
                    visited[next_node] = 1
                else:
                    pass
            elif visited[next_node] == 1:
                count += 1
        # print(graph[current_node])
    else:
        pass
    if len(graph[current_node]) == count and len(graph[current_node]) != 0:
        num_res.append(current_node)
        # print(num_res)
    else:
        pass
    print(len(num_res))
