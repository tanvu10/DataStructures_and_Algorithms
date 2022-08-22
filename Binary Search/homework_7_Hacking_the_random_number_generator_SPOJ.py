def binary_search(list_num, num):
    left = 0
    right = len(list_num) - 1
    while left <= right:
        mid = (left + right)//2
        if list_num[mid] == num:
            return mid
        elif list_num[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1

len_list, k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list = sorted(num_list)
count_pair = 0
# while len(num_list) > 0:
for i in range(len(num_list)):
    first_num = num_list[i]
    second_num = first_num + k
    index = binary_search(num_list, second_num)
    if index != -1:
        count_pair +=1
print(count_pair)