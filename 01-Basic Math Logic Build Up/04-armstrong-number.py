from math import *
n = int(input())
num = n
# def count(num):
#     return int(log10(num)+1)
length = len(str(n))
result = 0
while num>0:
    digit = num%10
    digit = digit**length
    result = result + digit
    num//=10
if(result==n):
    print(True)
else:
    print(False)