arr = [0,1,1,0,1,1,1,0,1,1,1,1]
count = 0
maxcoun = 0
for i in arr:
    if i == 1:
        count +=1
        maxcoun = max(count,maxcoun)
    else:
        count = 0
print(maxcoun)