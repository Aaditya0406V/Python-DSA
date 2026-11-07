lst = [1,2,3,2,3,4,5,3,4,9,9,9,9,9]
dict = {}
for i in range(0,len(lst)):
    if lst[i] in dict:
        dict[lst[i]]+=1
    else:
        dict.update({lst[i]:1})
for k,v in dict.items():
    print(f"{k} -> {v}")