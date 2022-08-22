import heapq
import math
num_case = int(input())
max_heap = []
min_heap = []
count = 0
for _ in range(num_case):
    command_rate = list(map(int, input().split()))

    if len(command_rate) == 2:
        count += 1
        heapq.heappush(min_heap, command_rate[1])
    elif len(command_rate) == 1:
        percentile = count//3
        if percentile > 0:
            if len(max_heap) > 0 and len(min_heap) > 0:
                max_num = - heapq.heappop(max_heap)
                min_num = heapq.heappop(min_heap)
                while max_num > min_num:
                    heapq.heappush(max_heap, -min_num)
                    heapq.heappush(min_heap, max_num)
                    max_num = - heapq.heappop(max_heap)
                    min_num = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -max_num)
                heapq.heappush(min_heap, min_num)
                if len(min_heap) > percentile:
                    while len(min_heap) > percentile:
                        heapq.heappush(max_heap, -heapq.heappop(min_heap))
                elif len(min_heap) < percentile:
                    while len(min_heap) > percentile:
                        heapq.heappush(min_heap, -heapq.heappop(max_heap))
                print(min_heap[0])
            else:
                if abs(len(max_heap) - len(min_heap)) > 1:
                    if len(max_heap) > len(min_heap):
                        while (len(max_heap) - len(min_heap)) > 1:
                            pop_num = - heapq.heappop(max_heap)
                            heapq.heappush(min_heap,pop_num)
                    elif len(max_heap) < len(min_heap):
                        while (len(min_heap) - len(max_heap)) > 1:
                            pop_num =  heapq.heappop(min_heap)
                            heapq.heappush(max_heap,-pop_num)

                if len(min_heap) > percentile:
                    while len(min_heap) > percentile:
                        heapq.heappush(max_heap, -heapq.heappop(min_heap))
                elif len(min_heap) < percentile:
                    while len(min_heap) > percentile:
                        heapq.heappush(min_heap, -heapq.heappop(max_heap))
                print(min_heap[0])
            # print('max', max_heap)
            # print('min', min_heap)
        else:
            print('No reviews yet')


