
input_ = int(input())
list_input = []
for _ in range(input_):
    input__ = list(input())
    list_input.append(input__)
# input_list = list(input())
# print(list_input)

def debug_(list_input):
    stack_1 =[]
    stack_2 = []
    counter = 0
    for i in range(len(list_input)):
        if list_input[i] == '<':
            stack_1.append(list_input[i])
        elif list_input[i] == '>':
            if len(stack_1) != 0:
                stack_1.pop()
                if len(stack_1) ==0:
                    counter = i+1
            else:
                return print(counter)
    return print(counter)
for input_i in list_input:
    debug_(input_i)
