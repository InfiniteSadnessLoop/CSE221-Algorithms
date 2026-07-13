def binary_tree(arr, start, end):

    if start > end:
        return

    mid = start + (end - start) // 2 
    print(arr[mid], end=" ")

    binary_tree(arr, mid + 1, end)
    binary_tree(arr, start, mid - 1)

n = int(input())
arr = list(map(int, input().split()))
binary_tree(arr, 0, n - 1)
