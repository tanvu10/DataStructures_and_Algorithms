L, R = [],[]
num_list = []
for _ in range(8):
    a, b = map(int, input().split())
    num_list.append([a,b])
    L.append(a)
    R.append(b)

def eight_points(left_list, right_list, num_list):
    left_dic = {}
    right_dic ={}
    for key in left_list:
        left_dic[key] = 0
    for key in right_list:
        right_dic[key] = 0

    total_list = []
    mid_point_right = sorted(right_dic.keys())
    mid_point_left = sorted(left_dic.keys())
    # print(mid_point_left)
    # print(mid_point_right)
    if len(mid_point_left) == 3 and len(mid_point_right) ==3:
        for i in range(len(mid_point_left)):
            for j in range(len(mid_point_right)):
                if i == 1 and j == 1:
                    pass
                else:
                    total_list.append([mid_point_left[i],mid_point_right[j]])
        # print(total_list)
        for i in total_list:
            if i in num_list:
                num_list.remove(i)
            else:
                return print('ugly')

        if len(num_list) == 0:
            return print('respectable')
        else:
            return print('ugly')
    else:
        return print('ugly')

eight_points(L, R, num_list)





