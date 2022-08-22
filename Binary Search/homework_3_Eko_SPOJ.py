num_tree, need_wood = map(int, input().split())
list_tree = list(map(int, input().split()))
list_tree = sorted(list_tree)

height = 0
def binary_search_median(list_tree, need_wood):
    left = 0
    right = list_tree[-1]
    while left < right:
        mid = (left + right)/2
        sum_check = sum([(a-mid) for a in list_tree if a > mid])
        if round(sum_check,1) == need_wood:
            return int(mid)
        elif sum_check > need_wood:
            left = mid
        else:
            right = mid
    return int(mid)

index = binary_search_median(list_tree, need_wood)
print(index)