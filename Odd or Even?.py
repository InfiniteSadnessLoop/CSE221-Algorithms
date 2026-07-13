inp = int(input())
for i in range(inp):
    num = int(input())
    if num % 2 == 0:
        print(f"{num} is an Even number.")
    if num % 2 != 0:
        print(f"{num} is an Odd number.")
