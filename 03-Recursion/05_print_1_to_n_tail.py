# print 1 to n by tail recursion

def fun(n):
    if n == 0:
        return
    fun(n-1)
    print(n)
fun(4)