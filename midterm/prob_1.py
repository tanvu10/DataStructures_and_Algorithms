num_word = int(input())
word = list(input())
set = set(word)
# print(set)
check_list = [False]*179
for w in set:
    if ord(w) < 91 and check_list[ord(w)+32] == False:
        check_list[ord(w)] = True
    if ord(w) > 91 and check_list[ord(w)-32] == False:
        check_list[ord(w)] = True
check_sum = sum(check_list)
# print(sum(check_list))
if check_sum >= 26:
    print('YES')
else:
    print('NO')