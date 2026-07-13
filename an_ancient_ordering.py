import sys
input = sys.stdin.readline

n = int(input())
w = [input().strip() for _ in range(n)]

g = [[] for _ in range(26)]
deg = [0] * 26
used = [0] * 26

for word in w:
    for c in word:
        used[ord(c) - 97] = 1

ok = 1
for i in range(n - 1):
    a, b = w[i], w[i + 1]
    j = 0
    while j < len(a) and j < len(b) and a[j] == b[j]:
        j += 1
    if j < len(a) and j < len(b):
        u, v = ord(a[j]) - 97, ord(b[j]) - 97
        g[u].append(v)
        deg[v] += 1
    elif len(a) > len(b):
        ok = 0
        break

if not ok:
    print(-1)
    exit()

h = [0] * 26
sz = 0

for i in range(26):
    if used[i] and deg[i] == 0:
        h[sz] = i
        sz += 1

for i in range(sz // 2 - 1, -1, -1):
    j = i
    while 2 * j + 1 < sz:
        l, r = 2 * j + 1, 2 * j + 2
        m = l
        if r < sz and h[r] < h[l]: m = r
        if h[j] <= h[m]: break
        h[j], h[m] = h[m], h[j]
        j = m

res = []
while sz:
    u = h[0]
    res.append(chr(u + 97))
    sz -= 1
    h[0] = h[sz]

    j = 0
    while 2 * j + 1 < sz:
        l, r = 2 * j + 1, 2 * j + 2
        m = l
        if r < sz and h[r] < h[l]: m = r
        if h[j] <= h[m]: break
        h[j], h[m] = h[m], h[j]
        j = m

    for v in g[u]:
        deg[v] -= 1
        if deg[v] == 0:
            h[sz] = v
            k = sz
            sz += 1
            while k and h[(k - 1) // 2] > h[k]:
                h[k], h[(k - 1) // 2] = h[(k - 1) // 2], h[k]
                k = (k - 1) // 2

print(''.join(res) if sum(used) == len(res) else -1)
