nb = list(map(int,input().split()))
time_array = list(map(int,input().split()))

time_available= nb[1]

def greedy_book(time_array, time_available):
    # time_array = sorted(time_array)
    counter = 0
    for i in range(len(time_array)):
        if time_available >= time_array[i]:
            counter += 1
            time_available = time_available - time_array[i]
        else:
            return counter
    return counter


def max_counter(time_array, time_available):
    max_counter = 0
    for i in range(len(time_array)):
        counter = greedy_book(time_array[i:], time_available)
        if counter >= max_counter:
            max_counter = counter
    return print(max_counter)


def optimization_greedy_book(time_array, time_available):
    max_counter = 0
    left_index = 0
    sum = 0
    for right_index in range(len(time_array)):
        # print('li', left_index)
        # print('ri', right_index)
        # print(time_array[left_index: right_index+1])
        sum += time_array[right_index]
        if sum > time_available:
            sum -= time_array[left_index]
            left_index+=1
        max_counter = max(max_counter, right_index - left_index + 1)
    return print(max_counter)


max_counter(time_array, time_available)
optimization_greedy_book(time_array, time_available)
