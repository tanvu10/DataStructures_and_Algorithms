

def balancing(list_num):
    max_counter = 0
    slow_index = 0
    for fast_index in range(len(list_num)):
        while set(list_num[slow_index:fast_index+1]) > 2:
            slow_index +=1
        counter = fast_index - slow_index +1
        print('slow_fast', slow_index, fast_index)
        max_counter = max(counter, max_counter)
        print('counter_max_counter', counter, max_counter)
    return print(max_counter)
#