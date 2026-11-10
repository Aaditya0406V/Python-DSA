lst = [1,3,4,2,8,4,6,3,5,2,9,0]

def selection_sort(lst):
    n = len(lst)
    for i in range(0,n-1):
        min_index = i
        for j in range(i+1,n):
            if lst[min_index] > lst [j]:
                min_index = j
        lst[i],lst[min_index] = lst[min_index],lst[i]
    return lst

print(selection_sort(lst))