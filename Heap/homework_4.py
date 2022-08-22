num_cases = int(input())
ID_list = {}
ID_change = {}
import heapq
some_heap = []
for _ in range(num_cases):
    ID, current_score, post, like, comment, share,  = map(int, input().split())
    new_score = 50*post + 5*like + 10*comment + 20*share
    score_change = new_score - current_score
    ID_list[ID] = current_score + score_change
    ID_change[ID] = -score_change
    heapq.heappush(some_heap, -score_change)
    #nlogn

from queue import Queue
# print(some_heap)
some_list = Queue()
for _ in range(5):
    some_list.put(heapq.heappop(some_heap))
# print(some_list)
# print(ID_list)


ID_change_key = sorted(ID_change, reverse=True)
while not some_list.empty():
    current_element = some_list.get()
    for key in ID_change_key:
        if ID_change[key] == current_element:
            ID_change_key.remove(key)
            print(key,ID_list[key])
            break
