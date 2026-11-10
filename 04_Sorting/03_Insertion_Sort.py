arr = [1,3,4,2,8,4,6,3,5,2,9,0]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1  # yaha already j define kara hai
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key 
    return arr 
print(insertion_sort(arr))
