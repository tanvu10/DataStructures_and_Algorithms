import math
nb = list(map(int, input().split()))
num_pass = nb[0]
k_try = nb[1]
password_list = []
for i in range(num_pass):
    enter = input()
    password_list.append(enter)
real_password = input()

# print(password_list)

def password_cracker(num_try, pass_list, real_pass):
    time = 0
    slack_pass = 0
    equal_pass = 0
    for password in pass_list:
        # print(password)
        if len(password) == len(real_password):
            equal_pass += 1
        if len(password) < len(real_pass):
            slack_pass += 1
    for i in range(1,slack_pass+equal_pass):
        time+=1
        if i % num_try == 0:
            time+=5
    pernalty_time = math.floor(slack_pass/num_try)*5 + slack_pass
    best_time = pernalty_time + 1
    worst_time = time + 1
    print(best_time, worst_time)



password_cracker(k_try, password_list, real_password)

