num_testcase = int(input())
for _ in range(num_testcase):
    n, m = map(int, input().split())
    list_candy = list(map(int, input().split()))
    candy_set = set(list_candy[:n])
    remaining_candy = list_candy[n:]
    for candy in remaining_candy:
        if candy in candy_set:
            print('YES')
        else:
            print('NO')
            candy_set.add(candy)