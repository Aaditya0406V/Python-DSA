def fun(num):
    if num == 0 or num == 1:
        return num
    return fun(num-1) + fun(num-2)
ans = fun(0)
print(ans)
ans = fun(1)
print(ans)
ans = fun(2)
print(ans)
ans = fun(3)
print(ans)
ans = fun(4)
print(ans)
ans = fun(5)
print(ans)