s = 'etdrxhtrgkycacnzdthxsafjzdagnfsjf'
q = ['a','s','d','f']

dict = {}

for ch in s:
    dict[ch] = dict.get(ch,0) + 1
for ch in q:
    if dict.get(ch):
        print(f"{ch} -> {dict[ch]}")
    else:
        print(f"{ch} -> 0")