num_testcase = int(input())
for _ in range(num_testcase):
    n, x = map(int, input().split())
    list_num = list(map(int, input().split()))
    set_a = set(list_num)
    if len(set_a) == x:
        print('Good')
    elif len(set_a) > x:
        print('Average')
    else:
        print('Bad')

