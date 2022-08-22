from copy import deepcopy

num_vertex = int(input())
dist_original = []
for _ in range(num_vertex):
    matrix_input = list(map(int, input().split()))
    dist_original.append(matrix_input)

del_vertex = list(map(int, input().split()))

def floyd_warshall(dist, num_vertex):
    dist1 = deepcopy(dist)
    for k in range(num_vertex):
        for i in range(num_vertex):
            for j in range(num_vertex):
                if dist1[i][k] == 10e9:
                    continue
                if dist1[k][j] != 10e9 and dist1[i][k] + dist1[k][j] < dist1[i][j]:
                    dist1[i][j] = dist1[i][k] + dist1[k][j]
    return dist1, dist

length_save = []
for delete_vertex in del_vertex:
    real_vertex = delete_vertex - 1
    dist_i, dist_original = floyd_warshall(dist_original, num_vertex)
    current_length = 0
    for i in range(num_vertex):
        for j in range(num_vertex):
            if dist_i[i][j] != 10e9:
                current_length += dist_i[i][j]

            if i == real_vertex or j == real_vertex:
                if i == j == real_vertex:
                    dist_original[i][j] = 0
                else:
                    dist_original[i][j] = 10e9

    length_save.append(current_length)

print(*length_save)