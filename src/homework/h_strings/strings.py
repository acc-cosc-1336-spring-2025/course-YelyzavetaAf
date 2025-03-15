def get_hamming_distance(dna1, dna2):
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    return distance
    

def get_dna_complement(dna):
    complement = ""
    for base in dna:
        if base == 'A':
            complement += 'T'
        elif base == 'T':
            complement += 'A'
        elif base == 'C':
            complement += 'G'
        elif base == 'G':
            complement += 'C'


    reverse_complement = ""
    for i in range(len(complement) - 1, -1, -1):
        reverse_complement += complement[i]


    return reverse_complement