
tmp = input().split()

cow = tmp[0]
nos = len(cow)
n   = nos

i   = int(tmp[1])

# get enough of n, so that n >= i!
while i > n:
    n += n

# reduce i conditionally!
while i > nos:
    half = n//2
    if i == half+1:
        i = half
    elif i > half+1:
        i = i-half-1
    n = half

# now i <= nos
print(cow[i-1])
