from math import exp, sin, cos, tan
import sys
sys.setrecursionlimit(1000000)
def value(p, q, r, s, t, u, x):
    return p*exp(-x) + q*sin(x) + r*cos(x) + s*tan(x) + t*(x**2) + u
def binary_search(p, q, r, s, t, u, left, right):
    while left < right:
        mid = (left + right) / 2
        if 0 <= value(p, q, r, s, t, u, mid) <=  10**(-7):
            return print("{:.4f}".format(mid))
        if value(p, q, r, s, t, u, mid) <= 0 and value(p, q, r, s, t, u, right) >= 0:
            left = mid
        elif value(p, q, r, s, t, u, mid) <= 0 and value(p, q, r, s, t, u, left) >= 0:
            right = mid
        elif value(p, q, r, s, t, u, mid) >= 0 and value(p, q, r, s, t, u, right) <= 0:
            left = mid
        elif value(p, q, r, s, t, u, mid) >= 0 and value(p, q, r, s, t, u, left) <= 0:
            right = mid
        else:
            break
    return print('No Solution')

while True:
    try:
        p, q, r, s, t, u = map(int, input().split())
        binary_search(p, q, r, s, t, u, 0, 1)
    except:
        break