n_x = list(map(int, input().split()))
chapter_list = list(map(int, input().split()))

number_subject = n_x[0]
max_time_learn = n_x[1]

def least_time(chapter_list, max_time_learn):
    time_list = [i for i in (range(max_time_learn,0,-1))]
    chapter_list = sorted(chapter_list)
    time = 0
    for i in range(len(chapter_list)):
        if i >= len(time_list):
            time+=chapter_list[i]
        else:
            time+= chapter_list[i]*time_list[i]



    return print(time)
least_time(chapter_list, max_time_learn)

