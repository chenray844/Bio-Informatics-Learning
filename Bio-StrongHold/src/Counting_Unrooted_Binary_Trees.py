def count_unrooted_binary_trees(n):
    '''Returns the number of unrooted binary trees with n leaves.'''
    # The total number is just the double factorial (2n -5)!!
    return reduce(lambda a, b: a*b % 10**6, xrange(2*n-5, 1, -2))

n = 868
print count_unrooted_binary_trees(n)