num, sum = map(int, input().split())
arr = list(map(int, input().split()))
def sum1(num,sum,arr):
    i=0
    j=len(arr)-1
    flag=False
    while i<j:
        if arr[i]+arr[j]==sum:
            print((f"{i+1} {j+1}"))
            flag=True
            break
        elif arr[i]+arr[j]<sum:
            i=i+1
        elif arr[i]+arr[j]>sum:
            j=j-1
    if flag==False:
        print(-1)
sum1(num,sum,arr)
