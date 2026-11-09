s = "nition"

def fun(s,left,right):
    if left>=right:
        return True
    if s[left] != s[right]:
        return False
    return fun(s,left+1,right-1)   
print(fun(s,0,len(s)-1)) 