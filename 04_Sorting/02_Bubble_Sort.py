lst = [1,3,4,2,8,4,6,3,5,2,9,0]

def bubble_sort(lst):
    n = len(lst)
    for i in range(n-2,-1,-1): # here used -1 for end value beacuse the end value will be 0
        is_Swap = False
        for j in range(0,i+1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                is_Swap = True
        if is_Swap == False:
            break
    return lst
print(bubble_sort(lst))

# Time Complexity = O(N^2)
# Space Complexity = O(1)
