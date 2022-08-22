case = 1
while True:
    num_currency = int(input())
    if num_currency == 0:
        break
    currency_dic = {}
    for i in range(num_currency):
        name = input()
        currency_dic[name] = i
    dist = [[10e9]*num_currency for _ in range(num_currency)]
    for i in range(num_currency):
        for j in range(num_currency):
            dist[i][j] = 0

    num_exchange = int(input())
    for _ in range(num_exchange):
        start, exchange_rate, stop = input().split()
        dist[currency_dic[start]][currency_dic[stop]] = - float(exchange_rate)

    # print(dist)
    for k in range(num_currency):
        for i in range(num_currency):
            for j in range(num_currency):
                if dist[i][k] == 10e9:
                    continue
                if dist[k][j] != 10e9 and -abs(dist[i][k]*dist[k][j]) < dist[i][j]:
                    dist[i][j] = -abs(dist[i][k]*dist[k][j])

    arbitrage = False
    for i in range(num_currency):
        if dist[i][i] < -1:
            arbitrage = True

    # print(dist)
    if arbitrage:
        print(f'Case {case}: Yes')
    else:
        print(f'Case {case}: No')
    case += 1
    input()