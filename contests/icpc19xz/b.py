def pre():
    pass

def f(n,k):
    global l2, l3
    if k==1:
        return 2 if n>1 else 1
    return l2[n] if k==2 else l3[n]

pre()
T = int(input())
for i in range(T):
    n,k = list(map(int,input()))
    print(f(n,k))
