def binary_string(arr):
    output = -1
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == '1':
            output = mid + 1
            right = mid - 1 
        else:
            left = mid + 1

    return output

test = int(input())
for i in range(test):
    arr = input().strip()  
    print(binary_string(arr))
    
