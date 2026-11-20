arr = [2,0,0,5,3,4,6,0,6,0,3,0]

i = 0
while arr[i] ==0:
    i+=1
j = i+1
while j<len(arr):
    if arr[j]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
    j+=1

print(arr)