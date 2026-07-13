def bubbleSort(arr):
    for i in range(len(arr)-1):
        sorted = True
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False        
        if sorted == True:
            break
    print(*arr)
le = int(input())    
arr = list(map(int, input().split()))    
bubbleSort(arr) 
