def JRscedule(arr):
  n= len(arr)
  for i in range(len(arr)):
    for j in range(len(arr)-i-1):
      if arr[j][0] > arr[j+1][0]:
         arr[j], arr[j+1] = arr[j+1], arr[j]
      if arr[j][0] == arr[j+1][0] and arr[j][2] < arr[j+1][2]:
          arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr
length = int(input())
alist = []
def timing(time):
  hr,min = map(int, time.split(":"))
  return min+(hr*60)
for i in range(length):
  line = input().split()
  train=line[0]
  dest=line[4]
  time=timing(line[6])
  alist.append([train,dest,time])
JRscedule(alist)
for i in range(length):
  print(f"{alist[i][0]} will departure for {alist[i][1]} at {alist[i][2]//60:02d}:{alist[i][2]%60:02d}")
