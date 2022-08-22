from queue import Queue
num_test = int(input())
for _ in range(num_test):
    num_doc, current_pos = map(int, input().split())
    priority_list = list(map(int, input().split()))

    def main(num_doc, current_pos):
        q = Queue()
        dic_map = {}
        list_priority_count = [0] * 10
        for i in range(num_doc):
            q.put(i)
            dic_map[i] = priority_list[i]
        for j in priority_list:
            list_priority_count[j] += 1
        # print(list_priority_count)
        time = 0
        while True:
            for i in range(9,-1,-1):
                while list_priority_count[i] != 0:
                    current_i = q.get()
                    if dic_map[current_i] == i:
                        time += 1
                        if current_i == current_pos:
                            return print(time)
                        list_priority_count[i] -= 1
                    else:
                        q.put(current_i)

    main(num_doc,current_pos )

