s = 'sacdvsbfdgfnhgjmhffdyuyuyuyyy'
q = ['d','a','y','u']

freq = [0]*26

for ch in s:
    asci_val = ord(ch)
    index = asci_val-97
    freq[index]+=1
for ch in q:
    asci_val = ord(ch)
    index = asci_val-97
    print(freq[index])
