n = int(input())
nb = list(map(int, input().split()))

def Bear_and_Game(minute_list):
    current_watching_time = 0
    #update to the end of the list
    for i in range(len(minute_list)):
        if i == 0:
            if current_watching_time + 15 < minute_list[0]:
                return print(current_watching_time + 15)
            else:
                current_watching_time = minute_list[0]
        else:
            if current_watching_time + 15 >= minute_list[i]:
                if current_watching_time + 15 < 90:
                    current_watching_time = minute_list[i]
                else:
                    return print(90)
            else:
                return print(current_watching_time + 15)
    #update later time
    if current_watching_time + 15 < 90:
        return print(current_watching_time+15)
    else:
        return print(90)

Bear_and_Game(nb)
