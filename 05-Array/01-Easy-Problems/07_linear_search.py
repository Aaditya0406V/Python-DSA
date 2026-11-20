arr = [23,52,4,6,24,56,33,99,32]

index = -1

key = 991
i = 0
while i<len(arr):
    if arr[i] == key:
        index = i
        break
    i+=1
print(index)