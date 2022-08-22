n, k = map(int,input().split())
energy_list = list(map(int,input().split()))
energy_list = sorted(energy_list)

# def binary_greedy_search(energy_list):
#     left = energy_list[0]
#     right = energy_list[n - 1]
#     while left < right:
#         mid = (left + right)/2
#         print(mid)
#         lower_sum = 0
#         upper_sum = 0
#         remaining = 0
#         for i in range(len(energy_list)):
#             if energy_list[i] < mid:
#                 lower_sum += energy_list[i]
#             elif energy_list[i] > mid:
#                 remaining += (energy_list[i] - mid)
#                 upper_sum += mid
#         if 0 <= abs(lower_sum + remaining*(100-k)/100 - upper_sum) <= 10**(-6):
#             return print(mid)
#         elif lower_sum + remaining*(100-k)/100 < upper_sum:
#             right = mid
#         else:
#             left = mid
#     return print(left)

def binary_greedy_search(energy_list):
    left = energy_list[0]
    right = energy_list[n - 1]
    while left < right:
        mid = (left + right)/2
        # print(mid)
        lower_sum = 0
        upper_sum = 0
        for i in range(len(energy_list)):
            if energy_list[i] < mid:
                lower_sum += (mid - energy_list[i])
            elif energy_list[i] > mid:
                upper_sum += (energy_list[i] - mid)
        if 0 <= abs(upper_sum - upper_sum*k/100 - lower_sum) <= 10**(-6):
            return print(mid)
        elif upper_sum - upper_sum*k/100 < lower_sum:
            right = mid
        else:
            left = mid
    return print(left)


binary_greedy_search(energy_list)