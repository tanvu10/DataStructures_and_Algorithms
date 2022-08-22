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
