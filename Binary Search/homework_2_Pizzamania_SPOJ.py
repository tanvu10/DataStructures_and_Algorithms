num_testcase = int(input())
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

for _ in range(num_testcase):
    num_friend, pizza_price = map(int, input().split())
    money_list = list(map(int, input().split()))
    money_list = sorted(money_list)
    count_pair = 0
    while len(money_list) > 0:
        # first_num = money_list[-1]
        first_num = money_list.pop()
        second_num = pizza_price - first_num
        index = binary_search(money_list, second_num)
        if index != -1:
            money_list.pop(index)
            count_pair +=1
    print(count_pair)