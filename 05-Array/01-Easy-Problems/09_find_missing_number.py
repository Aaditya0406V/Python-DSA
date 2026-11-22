arr = [0,1,3,2,5,6,4,8]
def misNum(arr):
    n = len(arr)
    sum = n*(n+1)//2
    for i in arr:
        sum = sum - i
    return sum
print(misNum(arr))