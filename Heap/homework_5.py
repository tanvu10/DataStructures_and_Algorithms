import heapq
num_date = int(input())
max_heap = []
min_heap = []
max_track_heap = []
min_track_heap = []
total_cost = 0
count = 0
for _ in range(num_date):
    num_bill = list(map(int, input().split()))
    for i in range(1,len(num_bill)):
        heapq.heappush(max_heap, - num_bill[i])
        heapq.heappush(min_heap, num_bill[i])

    if len(min_track_heap) > 0:
        # max_bill =  -heapq.heappop(max_heap)
        while min_track_heap[0] == max_heap[0]:
                heapq.heappop(max_heap)
                heapq.heappop(min_track_heap)
                if len(min_track_heap) == 0:
                    break

        max_bill = -heapq.heappop(max_heap)
        heapq.heappush(max_track_heap, max_bill)
    else:
        max_bill = - heapq.heappop(max_heap)
        heapq.heappush(max_track_heap, max_bill)


    if len(max_track_heap) > 0:
        # max_bill =  -heapq.heappop(max_heap)
        while max_track_heap[0] == min_heap[0] and len(max_track_heap) > 0:
            heapq.heappop(min_heap)
            heapq.heappop(max_track_heap)
            if len(max_track_heap) == 0:
                break


        min_bill = heapq.heappop(min_heap)
        heapq.heappush(min_track_heap, - min_bill)
    else:
        min_bill = heapq.heappop(min_heap)
        heapq.heappush(min_track_heap, - min_bill)

    total_cost += (max_bill - min_bill)
print(total_cost)