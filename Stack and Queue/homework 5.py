input_list = list(input())
import queue

# input_list = list('((CH)2(OH2H)(C(H))O)3')
# print(input_list)


def bug__(input_list):
    stack = []
    point_dic = {'H' : 1, 'O': 16, 'C': 12}
    for ele in input_list:
        if ele == '(':
            stack.append(-1)
        elif ele.isnumeric():
            new_ele = int(ele)*stack.pop()
            stack.append(new_ele)
        elif ele == ')':
            sub_sum = 0
            while stack[-1] != -1:
                sub_sum += stack.pop()
            stack.pop()
            stack.append(sub_sum)
        else:
            stack.append(point_dic[ele])
    print(sum(stack))

bug__(input_list)