from decimal import Decimal
from StrongHold import MONOISOTOPIC_MASS_TABLE as protein_weight

def get_weight(prot):
    w = 0
    for p in prot:
        w += protein_weight[p]
    return w

# Read the input data.
with open('data/data.dat') as input_data:
    n = int(input_data.readline())
    protein = [input_data.readline().strip() for repeat in xrange(n)]
    weights = sorted([Decimal(line.strip()) for line in input_data.readlines()])

# Determine the multiplicities.
max_mult = -1
for p in protein:
    # Get the weights of all prefixes and suffixes of the current protein.
    current_weights = sorted([Decimal(get_weight(item)) for i in xrange(1, len(p)) for item in (p[i:],p[:-i])] + [Decimal(get_weight(p))])

    # Generate the desired multiset and count multiplicities in a dictionary.
    multiset = {}
    for cur in current_weights:
        for given in weights:
            if round(cur - given, 3) not in multiset:
                multiset[round(cur - given, 3)] = 1
            else:
                multiset[round(cur - given, 3)] += 1

    # Get the current maximum multiplicity.
    current_mult = max(multiset.values())

    # Update if we've found a new maximum multiplicity.
    if current_mult > max_mult:
        max_mult = current_mult
        max_protein = p

# Format the maximum paramters.
max_parameters = [str(max_mult), max_protein]

# Print and save the answer.
print '\n'.join(max_parameters)