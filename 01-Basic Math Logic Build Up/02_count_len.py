
inpt = 23456
num = inpt
# logic one 


# count = 0
# while num>0:
#     digit = num%10
#     count = count + 1
#     num=num//10
# print(count)

# logic 2

from math import *
def count(num):
    return int(log10(num)+1)
print(count(num))