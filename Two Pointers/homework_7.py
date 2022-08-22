nb = int(input())
time_array = list(map(int,input().split()))
# print(0%2)

def greedy_optimization(time_array):

    left_index = 0
    right_index = len(time_array) - 1
    p1 = time_array[0]
    p2 = time_array[-1]
    p1p = 1
    p2p = 1
    while abs(right_index-left_index) != 1:
        if p1 <= p2:
            left_index += 1
            p1 += time_array[left_index]
            p1p +=1
            # print('p1 turn', p1)
            # print('ri', right_index)
            # print('li', left_index)
        else:
            right_index -= 1
            p2 += time_array[right_index]
            p2p += 1
            # print('p2 turn',p2)
            # print('ri', right_index)
            # print('li', left_index)
        # elif p2 + time_array[right_index] < p1:
        #     p2 += time_array[right_index]
        #     right_index -= 1
        #     p2p += 1
        #     print('p2 turn')
        #     print('ri', right_index)
        #     print('li', left_index)

    return print(p1p, p2p)

greedy_optimization(time_array)




