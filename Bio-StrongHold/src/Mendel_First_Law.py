from __future__ import division

k = 27
m = 19
n = 22

def prob_dom(k,m,n):
    k,m,n = map(float, (k,m,n))
    t = k+m+n

    p_aa = n/t*((n-1)/(t-1)) + n/t*(m/(t-1))*0.5 + m/t*(n/(t-1))*0.5 +m/t*((m-1)/(t-1))*0.25
    p_A = 1.0-p_aa
    return p_A

print prob_dom(k,m,n)