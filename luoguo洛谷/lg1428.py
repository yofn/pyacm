
n  = int(input().split()[0])
sl = input().split()
fl = [int(s) for s in sl]

ol = []
for i in range(n):
    oi = 0
    for j in range(i):
        if fl[j]<fl[i]:
            oi += 1
    ol.append(oi)
print(' '.join(['%s'%i for i in ol]))

