def longest_subarray_sum(arr, sum):
    left = 0
    right = 0
    curr = 0
    maxind = 0    
    while right < len(arr):
        curr += arr[right]        
        while curr > sum and left <= right:
            curr -= arr[left]
            left += 1        
        if curr <= sum:
            maxind = max(maxind, right - left + 1)        
        right += 1    
    return maxind
l, sum = map(int,input().split())
arr = list(map(int, input().split()))
print(longest_subarray_sum(arr, sum))
