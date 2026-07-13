def merge(list1, list2):
    merged_list = []
    i, j = 0, 0
    inversions = 0 
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
            inversions += len(list1) - i  
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return merged_list, inversions 

def merge_sort(lst):
    if len(lst) == 1:
        return lst, 0 
    else:
        mid = (len(lst) - 1) // 2
        list1 = lst[0:mid + 1]
        list2 = lst[mid + 1:]
        list1, inv1 = merge_sort(list1)  
        list2, inv2 = merge_sort(list2)  
        merged_list, inv_merge = merge(list1, list2)  
        return merged_list, inv1 + inv2 + inv_merge 
length = int(input())
sample_data = list(map(int, input().split()))
sorted_data, inversion_count = merge_sort(sample_data)
print(inversion_count)
print(*sorted_data)
