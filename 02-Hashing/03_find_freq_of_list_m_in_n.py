# in this question we have to find the frequency of list m in list n



# constrains : -
# 0<n<=10
# n can have 10^8 elements
# m can have 10^8 elements

# optimal solution**

n =  [5,3,2,2,1,5,5,7,5,10]

m = [10,111,1,9,5,67,2]

hashlst = [0] * 11 

for i in n:
    hashlst[i]+=1
for i in m:
    if i<1 or i>10:
        print("0")
    else:
        print(hashlst[i])
