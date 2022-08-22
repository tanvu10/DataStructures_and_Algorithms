from queue import Queue
num_testcase = int(input())
input()
for _ in range(num_testcase):
    word_list = []
    while True:
        some_word = input()
        if some_word == '*':
            break
        word_list.append(some_word)
    # print(word_list)

    while True:
        try:
            x = input()
            start, end = x.split()
            length = len(start)
            start_index = 0
            stop_index = 0
            dictionary_word_list = {}
            dictionary_index_list = {}
            index_tracker = 0
            for index in range(len(word_list)):
                if len(word_list[index]) == length:
                    index_tracker += 1
                    if word_list[index] == start:
                        start_index = index_tracker
                    elif word_list[index] == end:
                        stop_index = index_tracker

                    dictionary_word_list[word_list[index]] = index_tracker
                    dictionary_index_list[index_tracker] = word_list[index]

            # print(dictionary_word_list)
            # print(dictionary_index_list)

            graph = [[] for _ in range(len(dictionary_word_list.keys())+1)]
            # print(graph)
            check_visited = [False]*(len(dictionary_word_list.keys())+1)

            for key_1 in dictionary_word_list.keys():
                for key_2 in dictionary_word_list.keys():
                    if key_1 != key_2:
                        graph[dictionary_word_list[key_1]].append(dictionary_word_list[key_2])

            distance = [0]*(len(dictionary_word_list.keys())+1)
            # print(graph)
            q = Queue()
            q.put((start_index, dictionary_index_list[start_index]))
            check_visited[start_index] = True
            while not q.empty():
                current_index, current_word = q.get()
                for next_index in graph[current_index]:
                    if not check_visited[next_index]:
                        some_count = 0
                        current_word = list(current_word)
                        next_word = list(dictionary_index_list[next_index])
                        for i in range(len(current_word)):
                            if current_word[i] != next_word[i]:
                                some_count += 1
                        if some_count == 1:
                            # print(dictionary_index_list[next_index])
                            check_visited[next_index] = True
                            distance[next_index] = distance[current_index] + 1
                            if next_index == stop_index:
                                break
                            q.put((next_index, dictionary_index_list[next_index]))

            print(start, end, distance[stop_index])
        except:
            break
    print()
#
# '2
#
# axe
# axi
# bxi
# cxi
# dxi
# dli
# dlx
# dls
# cls
# clx
# *
# axe axi
# axe clx
# axi cls
# axi dli
# dli cls
# cxi cls
#
# lip
# mad
# map
# maple
# may
# pad
# pip
# pod
# pop
# sap
# sip
# slice
# slick
# spice
# stick
# stock
# *
# spice stock
# may pod'