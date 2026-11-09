# print n to 1 by tail recursion

def fun(x,n):
    if n == 0:
        return
    fun(x+1,n-1)
    print(x)
fun(1,4)