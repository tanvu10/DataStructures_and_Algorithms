num = int(input())
list_num = list(map(int, input().split()))
import heapq

some_heap = []
for i in range(len(list_num)):
    if i < 2:
        print(-1)
        heapq.heappush(some_heap,-list_num[i])
    else:
        heapq.heappush(some_heap, -list_num[i])
        first = heapq.heappop(some_heap)
        second = heapq.heappop(some_heap)
        third = heapq.heappop(some_heap)
        print(-first*second*third)
        heapq.heappush(some_heap,first)
        heapq.heappush(some_heap, second)
        heapq.heappush(some_heap, third)



