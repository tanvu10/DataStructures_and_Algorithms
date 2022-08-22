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

num_string = int(input())
root = Node()
check = False
bad_string = None
for _ in range(num_string):
    word = input()
    minor_check = check_add(root, word)
    addWord(root, word)
    if minor_check:
        check = minor_check
        bad_string = word
        break
        # minor_check = False
if check:
    print('BAD SET')
    print(bad_string)
else:
    print('GOOD SET')