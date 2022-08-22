
input_list = []
A= True

while A:
    ip = input()
    if ip != '0 0':
        input_list.append(ip)
    else:
        break


population_list = []
cases_list= []
# print(list(input_list[0]))
print(input_list)

i = 0
while i < len(input_list):
    # print(input_list[i].split(' ')[0])
    if input_list[i].split(' ')[0].isnumeric():
        population_list.append(int(input_list[i].split(' ')[0]))
        j = 1
        sub_case = []
        # print(list(input_list[i])[2])
        while j <= int(input_list[i].split(' ')[1]):
            sub_case.append(input_list[i+j])
            j = j+1
            # print(cases_list)
            # print(j)
        cases_list.append(sub_case)
        i += j
        # print(i)

print(cases_list)
print(population_list)
# def debug_(list):

from queue import Queue
def debug_(population_num, cases):
    q = Queue()
    for i in range(population_num):
        q.put(i+1)

    print(list(q.queue))
    tem_stack = []
    j = 0
    while j < len(cases):
        if cases[j] == 'N':
            index = q.get()
            print(index)
            q.put(index)
            j+=1
        else:
            priority_num = int(cases[j].split(' ')[1])
            # print(priority_num)
            k = 0
            tem_stack =[]
            q.put(priority_num)
            after = q.get()
            # print(after)
            q.put(after)
            while after != priority_num:
                after = q.get()
                # print(after)
                q.put(after)
                k+=1
            j +=k




debug_(population_num=population_list[0], cases = cases_list[0] )
