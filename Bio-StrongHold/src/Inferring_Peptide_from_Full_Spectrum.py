import os
import sys
pw_dict = {
'A': 71.03711,
'C': 103.00919,
'D': 115.02694,
'E': 129.04259,
'F': 147.06841,
'G': 57.02146,
'H': 137.05891,
'I': 113.08406,
'K': 128.09496,
'L': 113.08406,
'M': 131.04049,
'N': 114.04293,
'P': 97.05276,
'Q': 128.05858,
'R': 156.10111,
'S': 87.03203,
'T': 101.04768,
'V': 99.06841,
'W': 186.07931,
'Y': 163.06333,
}

def find_weight_match(current_w, w_list):
	for weight in w_list:
		for item in pw_dict.items():
			if abs(item[1] - (weight - current)) < 0.01:
				return item[0]

	return -1

if __name__ == '__main__':
	with open('data/data.dat') as input_data:
		weights = [float(line.strip()) for line in input_data.readlines()]

	# Given that len(weights) = 2n+3
	n = (len(weights)-3)/2

	# Initialize Variables
	protein = ''
	current = weights[1]
	myw = [w for w in weights[2:]]

	# Iteratively build the protein.
	while len(protein) < n:
		temp = find_weight_match(current, myw)
		if temp == -1:
			break
		else:
			protein += temp
			current += pw_dict[temp]
			myw = filter(lambda w: w-current > 0, myw)

	# Print and save the output.
	print protein
