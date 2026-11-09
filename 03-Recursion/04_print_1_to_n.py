# print 1 to n using recursion 
 
def fun(i,n):
    if(i>n):
        return
    fun(i+1,n)
    print(i)
fun(1,4)