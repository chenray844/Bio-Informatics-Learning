def fib(n,k):
    a,b = 1,1
    for i in xrange(n-1):
        a,b = b, b+a*k
    return a

n = 32
k = 5
print fib(n,k)