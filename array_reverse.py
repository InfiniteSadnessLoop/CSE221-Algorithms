l, ind = map(int, input().split())
arr = list(map(int, input().split()))
rev_arr = arr[:ind]
out = rev_arr[::-1]
print(*out)
