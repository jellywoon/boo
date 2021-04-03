eng = int(input())
nem = int(input())
fr = int(input())
set1 = set()
set2 = set()
set3 = set()
c = []
for i in range( eng + nem + fr):
    name = input()
    c.append(name)

for k in c:
    if k not in set1 and k not in set2 and k not in set3:
        set1.add(k)
    elif k in set1 and k not in set2 and k not in set3:
        set2.add(k)
    elif k in set1 and k in set2 and k not in set3:
        set3.add(k)
    

inp = set1.intersection(set2)
res = inp.difference(set3)

print(len(res))

