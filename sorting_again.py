no_stu = int(input())
stu_id = list(map(int, input().split()))
mark = list(map(int, input().split()))
def selection(stu_id, mark):
  swaps = 0
  for i in range(len(stu_id)):
    minin = i
    for j in range(i+1, len(stu_id)):
      if mark[j] > mark[minin] or (mark[j]==mark[minin] and stu_id[j]<stu_id[minin]):
        minin = j
    if minin!=i:    
        stu_id[i], stu_id[minin] = stu_id[minin], stu_id[i]
        mark[i], mark[minin] = mark[minin], mark[i]
        swaps += 1
  return swaps  
print(f"Minimum swaps: {selection(stu_id,mark)}")  
for i in range(no_stu):
  print(f"ID: {stu_id[i]} Mark: {mark[i]}")
