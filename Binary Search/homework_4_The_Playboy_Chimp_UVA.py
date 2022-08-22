def left_binary(list_number, num):
    left = 0
    right = len(list_number)
    while left < right:
        mid = (left + right)//2
        if list_number[mid] < num:
            left = mid + 1
        else:
            right = mid
    return left

def right_binary(list_number, num):
    left = 0
    right = len(list_number)
    while left < right:
        mid = (left + right)//2
        if list_number[mid] > num:
            right = mid
        else:
            left = mid + 1 # [) open upperbound
    # print(mid)
    return left #if not found return index to insert that num

def riu_left(list_num, num):
    current_index = left_binary(list_num, num)
    if current_index == len(list_num):
        return list_num[current_index-1]
    if list_num[current_index] == num and current_index != 0:
        return list_num[current_index - 1]
    else:
        if current_index == 0:
            return 'X'
        else:
            return list_num[current_index -1]

def riu_right(list_num, num):
    current_index = right_binary(list_num, num)
    if current_index == 0:
        return list_num[0]
    if list_num[current_index-1] == num and current_index != len(list_num):
        return list_num[current_index]
    else:
        if current_index == len(list_num):
            return 'X'
        else:
            return list_num[current_index]

num_chim = int(input())
chim_height_list = list(map(int, input().split()))
chim_height_list = sorted(chim_height_list)
num_query = int(input())
luchu_height = list(map(int, input().split()))
for height in luchu_height:
    max_index = riu_left(chim_height_list, height)
    min_index = riu_right(chim_height_list, height)
    print(max_index, min_index)