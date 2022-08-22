num_testcase = int(input())
input()
for _ in range(num_testcase):
    list_tree = []
    count_tree_dic = {}
    while True:
        try:
            tree = input()
            if tree == '':
                break
            list_tree.append(tree)
        except EOFError:
            break
    for tree in list_tree:
        count_tree_dic[tree] = 0
    for tree in list_tree:
        count_tree_dic[tree] += 1
    sum_all = sum([value for value in count_tree_dic.values()])
    for key in sorted(count_tree_dic.keys()):
        print(key, '{:.4f}'.format(count_tree_dic[key]*100/sum_all))
    print()