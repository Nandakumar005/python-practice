def gcd (a,b):
    while b!=0:
        a,b = b,a%b
    return a
t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    d=list(map(int,input().split()))

prefix=[0]*n
suffix=[0]*n

prefix[0]=p[0]
for i in range(1,n):
    prefix[i]=gcd(prefix[i-1],p[i])

suffix[n-1]=p[n-1]
for i in range(n-2,-1,-1):
    suffix[i]=gcd(suffix[i+1],p[i])

ans = 0
for i in range(n):
    if n == 1:
        g = 0
    elif i == 0:
        g = suffix[1]
    elif i == n - 1:
        g = prefix[n - 2]
    else:
        g = gcd(prefix[i - 1], suffix[i + 1])

    ans = max(ans, gcd(g, d[i]))

print(ans)


