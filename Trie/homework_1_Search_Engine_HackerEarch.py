class Node:
    def __init__(self):
        self.countWord = 0
        self.priority = 0
        self.child = {}

def addWord(root, some_string, priority):
    tempo = root
    for character in some_string:
        if character not in tempo.child:
            tempo.child[character] = Node()
        tempo.priority = max(priority, tempo.priority)
        tempo = tempo.child[character]
    tempo.countWord += 1
    tempo.priority = max(priority, tempo.priority)

def findWord(root, some_string):
    tempo = root
    for character in some_string:
        if character not in tempo.child:
            return False
        tempo = tempo.child[character]
    return tempo.countWord > 0


def findWord_priority(root, some_string):
    tempo = root
    for character in some_string:
        if character not in tempo.child:
            return print(-1)
        tempo = tempo.child[character]
    return print(tempo.priority)


num_word, num_queries = map(int, input().split())
root = Node()
for _ in range(num_word):
    word, priority = input().split()
    addWord(root, word, int(priority))
for _ in range(num_queries):
    find_word = input()
    findWord_priority(root, find_word)