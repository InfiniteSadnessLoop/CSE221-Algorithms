num1=int(input())
list1=list(map(int,input().split()))
num2=int(input())
list2=list(map(int,input().split()))

def merge(a,b):
    res_list=[]
    i=0
    j=0    
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            res_list.append(a[i])
            i=i+1
        else:
            res_list.append(b[j])
            j=j+1

    while i<len(a):
            res_list.append(a[i])
            i=i+1

    while j<len(b):
            res_list.append(b[j])
            j=j+1
    return res_list
    
print(*(merge(list1,list2)))
