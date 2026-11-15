arr = [23,52,4,6,24,56,33,99,32,88]

i,j=0,len(arr)-1

largest1 = float("-inf")
largest2 = float("-inf")

for i in arr:
    if i > largest1:
        largest2 = largest1
        largest1 = i
    elif i < largest1 and i> largest2:
        largest2 = i

print(largest2)