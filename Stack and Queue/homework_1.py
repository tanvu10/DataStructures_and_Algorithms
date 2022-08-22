


num = int(input())
list_expression = []
for i in range(num):
    ex = list(input())
    list_expression.append(ex)
print(list_expression)



def debug_(list):
    RPN = ''
    stack = []
    for i in list:
        if i in ['*','/','+','-','^']:
            stack.append(i)
        elif i == ')':
            if len(stack) != 0:
                RPN+= stack[-1]
                stack.pop()
            else:
                pass
        elif i!= ')' and i!= '(':
            RPN+= i
    return print(RPN)

for i in list_expression:
    debug_(i)




