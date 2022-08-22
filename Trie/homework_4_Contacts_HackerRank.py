class Node:
    def __init__(self):
        self.countWord = 0
        self.child = {}

def addWord(root, some_string):
    tmp = root
    for s in some_string:
        if s not in tmp.child:
            tmp.child[s] = Node()
        tmp.countWord += 1
        tmp = tmp.child[s]
    tmp.countWord += 1

def findWord(root, some_string):
    tmp = root
    for s in some_string:
        if s not in tmp.child:
            return False
        tmp = tmp.child[s]
    return tmp.countWord > 0

def findWord_v2(root, some_string):
    tmp = root
    for s in some_string:
        if s not in tmp.child:
            return 0
        tmp = tmp.child[s]
    return tmp.countWord


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

num_operation = int(input())
root = Node()
for _ in range(num_operation):
    ope, word = input().split()
    if ope == 'add':
        addWord(root, word)
    if ope == 'find':
        num = findWord_v2(root, word)
        print(num)
