total_num = int(input())
list_num = list(map(int, input().split()))
list_num = sorted(list_num)
import math
if len(list_num) % 2 == 0:
    mid_num = len(list_num)/2
    median = list_num[mid_num] + list_num[mid_num-1]
else:
    if len(list_num) == 1:
        median = list_num[0]
    else:
        mid_num = math.floor(len(list_num) / 2)
        median = list_num[mid_num]
print(median)