input_1 = list(map(int, input().split()))
segment = list(map(int, input().split()))

dis = input_1[1]
# print('segment length', len(segment))
def arrray_segment(segment, dis):
    if dis ==1:
        return print(1,1)
    for left_index in range(len(segment)):
        num_list = [segment[left_index]]
        for right_index in range(left_index+1, len(segment)):
            if segment[right_index] == segment[left_index]:
                break
            if segment[right_index] not in num_list:
                num_list.append(segment[right_index])
                # print(num_list)
                if len(num_list) == dis:
                    return print(left_index+1, right_index+1)
    return print(-1,-1)


arrray_segment(segment, dis)


