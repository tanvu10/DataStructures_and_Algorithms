
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
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1

case = 1
while True:
    n, m = map(int, input().split())
    if m == n == 0:
        break
    makeSet(n)
    for _ in range(m):
        a, b = map(int, input().split())
        joinSet(a, b)
    for i in range(1,n+1):
        parent[i] = findSet(i)
    ans = set()
    for i in range(1, n+1):
        ans.add(parent[i])
    print(f'Case {case}: {len(ans)}')
    case += 1
