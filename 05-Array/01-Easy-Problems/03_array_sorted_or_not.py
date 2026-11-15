# arr = [23,52,4,6,24,56,33,99,32,88]
arr = [1,2,3,4,5,6,7,8,9]
is_sort = True
for i in range(0,len(arr)-1):
    if arr[i]>arr[i+1]:
        is_sort = False
        break

print(is_sort)