num_test = int(input())
for _ in range(num_test):
    num_student = int(input())
    num_relationship = int(input())

    graph = [[] for _ in range(num_student)]
    for _ in range(num_relationship):
        start, stop = map(int, input().split(' '))
        graph[start].append(stop)
        graph[stop].append(start)
    visited = [False]*num_student
    count_time = 0
    for student in range(num_student):
        if not visited[student]:
            count_time += 1
            stack = []
            stack.append(student)
            visited[student] = True
            while len(stack) > 0:
                current_student = stack.pop()
                for next_student in graph[current_student]:
                    if not visited[next_student]:
                        stack.append(next_student)
                        visited[next_student] = True

    print(count_time)
