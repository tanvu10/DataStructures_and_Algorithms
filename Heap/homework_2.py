from heapq import heappush, heappop
valheap = []
delheap = []

q = int(input().strip())
for i in range(q):
    lst = list(map(int, input().strip().split(' ')))
    if lst[0] == 1:
        heappush(valheap, lst[1])
    elif lst[0] == 2:
        if valheap[0] == lst[1]:
            heappop(valheap)
        else:
            heappush(delheap, lst[1])
    elif lst[0] == 3:
        check = bool(delheap)
        while check:
            if delheap[0] == valheap[0]:
                heappop(delheap)
                heappop(valheap)
                check = bool(delheap)
            else:
                check = False
        print (valheap[0])