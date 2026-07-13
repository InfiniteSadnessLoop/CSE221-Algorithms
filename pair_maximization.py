def max_val(arr):
  max=arr[0]
  max_sum=-(10**6)
  for i in range (1,len(arr)):
    if max + arr[i]**2>=max_sum:
      max_sum=max + arr[i]**2
    if arr[i]>max:
      max=arr[i]
  return max_sum
length = int(input())
arr = list(map(int, input().split()))  
print(max_val(arr))
