num_testcase = int(input())
for case in range(num_testcase):
    num_rung = int(input())
    rung_list = list(map(int, input().split()))

    def max_search(rung_list):
        if len(rung_list) == 1:
            return print(f'Case {case +1}: {rung_list[0]}')
        else:
            rung_list.insert(0,0)
            current_max = 0
            for i in range(1, len(rung_list)):
                some_max = rung_list[i] - rung_list[i - 1]
                if some_max == current_max:
                    current_max +=1
                else:
                    current_max = max(current_max, rung_list[i] - rung_list[i-1])
            return print(f'Case {case +1}: {current_max}')
    max_search(rung_list)