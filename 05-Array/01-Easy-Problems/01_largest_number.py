arr = [23,52,4,6,24,56,33,99,32]
largest = float("-inf")
for i in arr:
    largest = max(i,largest)
print(largest)