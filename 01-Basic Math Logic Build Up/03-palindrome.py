n = 1221
num = n
result = 0
while num>0:
    id = num %10
    result = (result*10) + id
    num//=10
if(result==n):
    print(True)
else:
    print(False)