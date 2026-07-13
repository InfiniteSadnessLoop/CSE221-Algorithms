def fast_power(base, power, modulus):
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        power //= 2
    return result
num_tests = int(input())
for _ in range(num_tests):
    a, n, m = map(int, input().split())   
    if a == 1:
        print(n % m)
    else:
        x = (a - 1) * m
        power_result = fast_power(a, n, x)
        numerator = (power_result - 1) % x
        k_value = numerator // (a - 1)
        print((a * k_value) % m)
