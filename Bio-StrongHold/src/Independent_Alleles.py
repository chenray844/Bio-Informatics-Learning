import math

def prob_het(k,N):
    ''' AaBb probability - true for all iterative combinations.
    Draw punnit squares to verify if you don't believe me.
    '''
    prob_AaBb = 4/16.0

    prob = []
    total = 2**k
    # summation of your general binomial probability function
    for r in xrange(N,(total+1)):
        prob.append(nCr(total,r)*(prob_AaBb**r)*((1-prob_AaBb)**(total-r)))
    return sum(prob)

# quick combinatorial function
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

if __name__ == '__main__':
    print prob_het(5,9)