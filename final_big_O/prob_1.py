num_job = int(input())
list_num = list(map(int, input().split()))
new_list_num = []
for i in range(len(list_num)):
    new_list_num.append((list_num[i], i +1))
new_list_num.sort(key = lambda new_list_num: new_list_num[0])
print(new_list_num)
def main(new_list_num):
    count = 0
    for i in range(1, len(new_list_num)):
        if new_list_num[i][0] == new_list_num[i-1][0]:
            count += 1
        if count == 2:
            print('YES')
            list_1 = []
            for j in range(len(new_list_num)):
                list_1.append(new_list_num[j][1])
            print(*list_1)
            count = 0
            for k in range(1, len(new_list_num)):
                if new_list_num[k][0] == new_list_num[k-1][0]:
                    count += 1
                    new_list_num[k], new_list_num[k-1] = new_list_num[k-1], new_list_num[k]
                    list_2 = []
                    for h in range(len(new_list_num)):
                        list_2.append(new_list_num[h][1])
                    print(*list_2)
                    new_list_num[k], new_list_num[k - 1] = new_list_num[k-1], new_list_num[k]
                if count == 2:
                    return
    print('NO')
    return
main(new_list_num)


