keys = list(input().split(' '))
given_key = int(keys[0])
wanted_key = int(keys[1])
num_key = int(input())
N_keys = list(input().split(' '))
N_keys = [int(key) for key in N_keys]
# print(given_key, wanted_key)
# print(N_keys)

from queue import Queue


def bug_(given_key, N_keys, wanted_key):
    q = Queue()
    point_dic_level = {}
    visited_set = set()
    visited_set.add(given_key)
    point_dic_level[given_key] = 0
    q.put(given_key)
    # merge_key = given_key
    while not q.empty():
        current_key = q.get()
        for some_key in N_keys:
            merge_key = (current_key * some_key) % 100000
            if merge_key != wanted_key and merge_key not in visited_set:
                q.put(merge_key)
                visited_set.add(merge_key)
                point_dic_level[merge_key] = point_dic_level[current_key] + 1
            else:
                if merge_key == wanted_key:
                    point_dic_level[merge_key] = point_dic_level[current_key] + 1
                    return print(point_dic_level[merge_key])
                else:
                    pass

    print(-1)


bug_(given_key, N_keys, wanted_key)