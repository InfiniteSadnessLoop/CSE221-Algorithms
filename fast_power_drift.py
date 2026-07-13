def fastmod(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        mid = fastmod(a, b//2)   
        return (mid * mid) % 107     
    return ((a * (fastmod(a, b - 1))) % 107)
a, b = map(int, input().split())
output = fastmod(a, b)
print(output)
