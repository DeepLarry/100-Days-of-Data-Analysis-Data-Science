# cook your dish here
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    t = 0
    for s in range(n, m, -1):
        t = t + s
    print(t)