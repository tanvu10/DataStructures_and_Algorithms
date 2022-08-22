class Node:
    def __init__(self):
        self.countWord = 0
        self.child = {}


def addWord(root, some_string):
    tmp = root
    for s in some_string:
        if s not in tmp.child:
            tmp.child[s] = Node()
        tmp = tmp.child[s]
    tmp.countWord += 1

def check_add(root, some_string):
    tmp = root
    for s in some_string:
        if s not in tmp.child:
            return False
        tmp = tmp.child[s]
        if tmp.countWord > 0:
            return True
    if len(tmp.child) != 0:
        return True
    return False


def findWord(root, some_string):
    tmp = root
    for s in some_string:
        if s not in tmp.child:
            return False
        tmp = tmp.child[s]
    return tmp.countWord > 0

def isLastword(node):
    return len(node.child) == 0

def isWord(node):
    return node.countWord != 0

def delWord(root, some_string, depth):
    #find if that word exist
    tmp = root
    #at base case - deepest: return True or False
    if depth == len(some_string):
        if tmp.countWord > 0:
            tmp.countWord -= 1
            return True
        else:
            return False
    pointed_char = some_string[depth]

    if pointed_char not in tmp.child:
        return False
    check = delWord(tmp.child[some_string[depth]], some_string, depth + 1)

    if check and isLastword(tmp.child[pointed_char]) and not isWord(tmp.child[pointed_char]) == 0:
        del tmp.child[pointed_char]
        return True
    else:
        return False

num_word = int(input())
length_list = list(map(int, input().split()))

def main(length_list):
    count_array = [0]*1001
    init_string = ''
    max_length = max(length_list)

    for i in length_list:
        count_array[i] += 1

    init_allowed_word = 2
    for i in range(1,max_length+1):
        count_word = count_array[i]
        if count_word > init_allowed_word:
            print('NO')
            return
        init_allowed_word = (init_allowed_word - count_word)*2

    root = Node()
    save_all_string = []
    for i in length_list:
        check_with_0 = check_add(root, some_string= init_string + '0')
        if check_with_0:
            addWord(root, some_string=init_string + '1')
            save_all_string.append(init_string + '1')
            init_string = init_string + '0'
        else:
            addWord(root, some_string=init_string + '0')
            save_all_string.append(init_string + '0')
            init_string = init_string + '1'

    print('YES')
    for index in length_list:
        print(save_all_string[index-1])

main(length_list)
