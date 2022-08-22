import heapq
from queue import Queue

while True:
    try:
        num_element = int(input())
        q = Queue()
        stack = []
        some_heap = []
        queue_vote = 0
        stack_vote = 0
        heap_vote = 0
        counter = 0
        for _ in range(num_element):
            command, num = map(int, input().split())
            if command == 1:
                q.put(num)
                stack.append(num)
                heapq.heappush(some_heap, -num)
            elif command == 2:
                counter += 1
                stack_num = stack.pop()
                queue_num = q.get()
                heap_num = -heapq.heappop(some_heap)
                if stack_num == num:
                    stack_vote += 1
                if queue_num == num:
                    queue_vote += 1
                if heap_num == num:
                    heap_vote += 1
        if heap_vote == queue_vote == counter or heap_vote == stack_vote == counter or queue_vote == stack_vote == counter:
            print('not sure')
        else:
            if heap_vote == counter:
                print('priority queue')
            elif stack_vote == counter:
                print('stack')
            elif queue_vote == counter:
                print('queue')
            else:
                print('impossible')
    except:
        break
