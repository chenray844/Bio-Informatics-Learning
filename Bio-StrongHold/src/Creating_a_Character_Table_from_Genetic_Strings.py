def char_table_from_strings(dna_list):
    '''Builds a character table from a given list of strings.'''
    ch_table = set()
    for i, ch in enumerate(dna_list[0]):
        # Mark the on/off taxa based on the ith character of each sequence.
        ch_array = [int(dna[i] == ch) for dna in dna_list]
        if 1 < sum(ch_array) < len(dna_list)-1:  # Check nontrivial.
            ch_table.add(''.join(map(str,ch_array)))

    return ch_table


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/data.dat') as input_data:
        dna_list = [line.strip() for line in input_data.readlines()]

    # Get the character table.
    character_table = char_table_from_strings(dna_list)

    # Print and save the answer.
    print '\n'.join(character_table)

if __name__ == '__main__':
    main()