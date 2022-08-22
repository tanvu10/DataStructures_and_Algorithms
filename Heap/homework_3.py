import heapq
while True:
    num_element = int(input())
    if num_element == 0:
        break
    else:
        some_heap = []
        list_num = list(map(int, input().split()))
        total_sum_list = 0
        for el in list_num:
            heapq.heappush(some_heap, el)
        total_cost = 0
        while len(some_heap) > 0:
            if len(some_heap) == 1 :
                break
            first_num = heapq.heappop(some_heap)
            second_num = heapq.heappop(some_heap)
            total_cost += (first_num + second_num)
            heapq.heappush(some_heap, first_num+second_num)
        # total_cost = total_cost - some_heap[0]
        print(total_cost)