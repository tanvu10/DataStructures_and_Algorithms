input_list = []
A= True

while A:
    ip = input()
    if ip != '0':
        input_list.append(ip)
    else:
        break

# print(input_list[1].split(' ')[:-1])
true_input = input_list[1].split(' ')[:-1]
true_input = [int(i) for i in true_input]
# print(true_input)
def debug_(input_list):
    stack = []
    order_list =[]
    index_tracker = 0
    i = 0
    while i <= len(input_list)-1 :
        if input_list[i] - index_tracker == 1 :
            order_list.append(input_list[i])
            index_tracker+=1
            i+=1
        else:
            if input_list[i] - index_tracker > 1:
                stack.append(input_list[i])
                i+=1
            elif input_list[i] - index_tracker > 1 and len(stack) != 0:
                order_list.append(stack.pop())
                i += 1
                index_tracker+=1

    # print(order_list)
    while len(stack) != 0:
        for i in range(len(stack)):
            order_list.append(stack.pop())

    if order_list == sorted(input_list):
        return print('yes')
    else:
        return print('no')
debug_(true_input)