s = list(input())
t = list(input())
s_dic_1 = {}
t_dic_1 = {}
s_dic_2 = {}
t_dic_2 = {}

for char in t:
    t_dic_1[ord(char)] = 0
    t_dic_2[ord(char)] = 0

for char in t:
    t_dic_1[ord(char)] += 1
    t_dic_2[ord(char)] += 1

yay_count = 0
whoop_count = 0
for char in s:
    if ord(char) in t_dic_1.keys():
        if t_dic_1[ord(char)] > 0:
            yay_count +=1
            t_dic_1[ord(char)] -= 1
            # print(char)
for char in s:
    if ord(char) in t_dic_2.keys() and t_dic_2[ord(char)] > 0:
        t_dic_2[ord(char)] -= 1
    else:
        if (ord(char) + 32) in t_dic_1.keys() and t_dic_1[ord(char) + 32] > 0:
            whoop_count += 1
            t_dic_1[ord(char) + 32] -= 1
        elif (ord(char) - 32) in t_dic_1.keys() and t_dic_1[ord(char) - 32] > 0:
            whoop_count += 1
            t_dic_1[ord(char) - 32] -= 1

print(yay_count, whoop_count)

