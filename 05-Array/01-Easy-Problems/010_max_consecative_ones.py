arr = [0,1,1,0,1,1,1,0,1,1,1,1]
count = 0
maxcount = 0
for i in arr:
    if i == 1:
        count +=1
        maxcount = max(count,maxcount)
    else:
        count = 0
print(maxcount)