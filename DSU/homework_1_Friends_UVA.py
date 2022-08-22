parent = []
ranks = []

def makeSet(n):
    global parent, ranks
    parent = [i for i in range(n+1)]
    ranks = [0 for _ in range(n+1)]
    return parent, ranks

def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]

def joinSet(u,v):
    up = findSet(u)
    vp = findSet(v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
        num[up] += num[vp]
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
        num[vp] += num[up]
    else:
        parent[up] = vp
        ranks[vp] += 1
        num[vp] += num[up]
num_testcase = int(input())
for _ in range(num_testcase):
    n, m = map(int, input().split())
    parent, ranks = makeSet(n)
    num = [1 for i in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        joinSet(a, b)

    ans = 0
    for i in range(n+1):
        if parent[i] == i and num[i] > ans:
            ans = num[i]
    print(ans)