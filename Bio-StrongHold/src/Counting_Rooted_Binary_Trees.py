
def count_unrooted_binary_trees(n):
    '''Returns the number of unrooted binary trees with n leaves.'''
    # The total number is just the double factorial (2n -5)!!
    return reduce(lambda a, b: a*b % 10**6, xrange(2*n-5, 1, -2))

def count_rooted_binary_trees(n):
    '''Returns the number of unrooted binary trees with n leaves.'''
    # Can transform an unrooted binary tree into a rooted binary tree by inserting
    # a node into any of its 2*n - 3 edges.
    return count_unrooted_binary_trees(n)*(2*n - 3) % 10**6




def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    n = 918

    # Get the number of unrooted binary trees.
    count = count_rooted_binary_trees(n)

    # Print and save the answer.
    print count

if __name__ == '__main__':
    main()