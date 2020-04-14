d = dict()

p = {"leo" : 1, "kiki" : 1, "eden" : 1}
c = {"eden" : 1, "kiki" : 1}


    
for x in p:
    d[x] = d.get(x, 0) + 1

for x in c:
    
    d[x] -= 1;

dnf = [k for k, v in d.items() if v>0]

print(dnf)