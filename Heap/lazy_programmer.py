import heapq
num_test = int(input())
for _ in range(num_test):
    num_case = int(input())
    all_list = []
    for _ in range(num_case):
        a, b, d = map(int, input().split())
        all_list.append(( - a, b, d))
    # print(all_list)
    all_list.sort(key = lambda sub_list: sub_list[2])
    # print(all_list)
    min_pay_heap = []
    current_time = 0
    current_money_pay = 0
    for i in range(len(all_list)):
        heapq.heappush(min_pay_heap, all_list[i])
        a_i, b_i, d_i = all_list[i]
        if current_time + b_i > d_i:
            pernalty = current_time + b_i - d_i
            while pernalty > 0:
                max_a, time, dead = heapq.heappop(min_pay_heap)
                if time > pernalty:
                    current_money_pay += -pernalty/max_a
                    time -= pernalty
                    pernalty = 0
                    heapq.heappush(min_pay_heap, (max_a, time, dead))
                else:
                    current_money_pay += -time/max_a
                    pernalty -=time
            current_time = d_i
        else:
            current_time += b_i
    current_money_pay = "{:.2f}".format(current_money_pay)
    print(current_money_pay)