def fun(sum,i,n):
    if n==0:
        print(sum)
        return
    fun(sum+i,i+1,n-1)
fun(0,1,3)