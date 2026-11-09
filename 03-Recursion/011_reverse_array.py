# reverse an array using the recursion 

lst = [1,4,6,3,2]

def fun(lst,left,right):
    if left>right:
        return 
    lst[left],lst[right] = lst[right],lst[left]
    fun(lst,left+1,right-1)

fun(lst,0,len(lst)-1)

print(lst) 
