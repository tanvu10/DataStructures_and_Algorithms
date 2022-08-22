nb = int(input())
time_array = list(map(int,input().split()))
# print(0%2)
import math
def greedy_time(time_array):
    p1 = 0
    p2 = 0
    left_index = 0
    right_index = len(time_array) - 1
    
    for i in range(len(time_array)):
        if i % 2 == 0:
            if time_array[left_index] > time_array[right_index]:
                p1 += time_array[left_index]
                left_index+=1
            else:
                p1 += time_array[right_index]
                right_index -=1
        else:
            if time_array[left_index] > time_array[right_index]:
                p2 += time_array[left_index]
                left_index+=1
            else:
                p2 += time_array[right_index]
                right_index -=1
    return print(p1, p2)

greedy_time(time_array)
