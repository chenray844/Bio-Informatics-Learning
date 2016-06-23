from math import sqrt

with open('data/data.dat') as input_data:
	A = map(float, input_data.read().strip().split())

B = [2*sqrt(i)-i for i in A]

print ' '.join(map(str,B))