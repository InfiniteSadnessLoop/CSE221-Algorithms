def count_num(arr):
  for i in range(query):
      right1 = len(arr)-1
      left1 = 0
      num1,num2 = map(int,input().split())
      while left1 <= right1:
          mid = (left1 + right1)//2
          if arr[mid] >= num1:
              right1 = mid - 1
          else:
              left1= mid+ 1
      left2 = 0
      right2 = len(arr) - 1
      while left2 <= right2:
          mid = (left2 + right2)//2
          if arr[mid] > num2:
              right2=mid-1
          else:
              left2=mid+1
      print(left2-left1)
length,query=map(int,input().split())
arr=list(map(int,input().split()))
count_num(arr)
