from copy import deepcopy
def main(num):
    if num == 1:
        return 1, 1
    start = 0
    init = 1
    while True:
        init += 2*start
        if init - start <= num <= init + start:
            x_start, y_start = start + 1, start + 1
            if num == init:
                return x_start, y_start
            if start % 2 == 0:
                if init < num < init + start:
                    new = deepcopy(init)
                    while num != new:
                        new += 1
                        x_start -= 1
                elif init - start < num < init:
                    new = deepcopy(init)
                    while num != new:
                        new -= 1
                        y_start -= 1
                elif num == init + start:
                    x_start -= start
                elif num == init - start:
                    y_start -= start
            else:
                if init < num < init + start:
                    new = deepcopy(init)
                    while num != new:
                        new += 1
                        y_start -= 1
                elif init - start < num < init:
                    new = deepcopy(init)
                    while num != new:
                        new -= 1
                        x_start -= 1
                elif num == init + start:
                    y_start -= start
                elif num == init - start:
                    x_start -= start
            return x_start, y_start
        start += 1


num_tc = int(input())
for case in range(num_tc):
    num = int(input())
    x, y = main(num)
    print(f'Case {case+1}: {x} {y}')