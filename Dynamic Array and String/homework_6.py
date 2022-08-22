import math
num_seg = int(input())
seg_list = []
for i in range(num_seg):
    enter = list(map(int,input().split()))
    seg_list.append(enter)

# print(seg_list)


def finding_segment(segment_list):
    min_a = min([elm[0] for elm in segment_list ])
    max_a = max([elm[1] for elm in segment_list ])

    index = -1
    for i in range(len(segment_list)):
        if segment_list[i][0] == min_a and segment_list[i][1] == max_a:
            return print(i+1)

    return print(index)

finding_segment(seg_list)



