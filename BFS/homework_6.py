from queue import Queue
while True:
    signal = input()
    if signal == '0 0':
        break
    else:

        row, col = map(int, (signal.split(' ')))
        matrix = [[] for _ in range(row)]
        for ro in range(row):
            sub_row = list(input().split(' '))
            matrix[ro] = sub_row

        print(matrix)
        visited_matrix = [[0]*col for _ in range(row)]

        count_dic = {}

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '1' and visited_matrix[r][c] == 0:
                    count = 0
                    qr = Queue()
                    qc = Queue()
                    qr.put(r)
                    qc.put(c)
                    visited_matrix[r][c] = 1
                    while not qr.empty():
                        current_row = qr.get()
                        current_col = qc.get()
                        row_direction = [0, 1, -1, 0]
                        col_direction = [-1, 0, 0, 1]
                        for i in range(len(row_direction)):
                            near_row = current_row + row_direction[i]
                            near_col = current_col + col_direction[i]
                            if 0 <= near_row < row and 0 <= near_col < col:
                                if matrix[near_row][near_col] == '1' and visited_matrix[near_row][near_col] == 0:
                                    qr.put(near_row)
                                    qc.put(near_col)
                                    visited_matrix[near_row][near_col] = 1
                        count+=1


                    if count in count_dic.keys():
                        count_dic[count] += 1
                    else:
                        count_dic[count] = 1

        # print(count_dic)
        total = 0
        for value in count_dic.values():
            total+= value
        print(total)

        for key in sorted(count_dic.keys()):
            print(key, count_dic[key])



