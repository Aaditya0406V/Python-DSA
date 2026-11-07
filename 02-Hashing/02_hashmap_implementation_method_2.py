lst = [1,2,3,2,3,4,5,3,4,9,9,9,9,9]
hashmap = {}
for i in range(0,len(lst)):
    hashmap[lst[i]] = hashmap.get(lst[i],0)+1  #here at when we write (lst[i],0)  -> get function returns a value so it checks ehather if the key is present or not, if key is present it is being incremented and if it is not the it returns 0 and new key is added and its value is set as 1 
for k,v in hashmap.items():
    print(f"{k} -> {v}")