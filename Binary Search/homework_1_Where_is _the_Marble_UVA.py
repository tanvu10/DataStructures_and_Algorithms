from bisect import bisect_left
def index(lst, elem):
    i = bisect_left(lst, elem)
    if i != len(lst) and lst[i] == elem:
        return i
    return -1

def BSFirst(list, num):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left+right)//2
        if list[mid] == num:
            #check leftmost and element on left
            if mid == left or list[mid-1] < num:
                return mid
        elif list[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1

count = 1
while True:
    num_marble, num_queries = map(int, input().split())
    if num_marble == num_queries == 0:
        break
    marble_list = []
    for _ in range(num_marble):
        marble_list.append(int(input()))
    marble_list = sorted(marble_list)
    print(f'CASE# {count}:')
    for _ in range(num_queries):
        queries = int(input())
        num_index = BSFirst(marble_list, queries)
        if num_index == -1:
            print(f'{queries} not found')
        else:
            print(f'{queries} found at {num_index+1}')
    count +=1
