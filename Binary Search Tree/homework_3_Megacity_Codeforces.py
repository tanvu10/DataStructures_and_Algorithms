from math import sqrt
num_city, current_population = map(int, input().split())

distance_list = []
for _ in range(num_city):
    x, y, num_pp = map(int, input().split())
    distance_list.append((num_pp, sqrt(x**2 + y**2)))
distance_list = sorted(distance_list, key = lambda x: x[1])
current_pp = 0
new_distance_list = []
for num_pp, distance in distance_list:
    current_pp += num_pp
    new_distance_list.append((current_pp, distance))

final_distance = -1
for add_pp, distance in new_distance_list:
    if current_population + add_pp >= 1000000:
        final_distance = distance
        break
print(final_distance)