# A collection of simple Python scripts I've been working on in my free time as a refresher for the Bioinformatics.
# ---------------------------------------------------------------------------------------------------------------------------------------------

# Compute the frequence of the pattern "CGCG" in a given text (string of nucleotides)
pattern = "CGCG"
text = "CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC"
count = text.count(pattern)
print(f"There are" , count, "CGCG patterns in", text, "which is", round(count * 100 / len(text)),\
       "%.")
# ---------------------------------------------------------------------------------------------------------------------------------------------

#  # Work out the most frequent 3-mer in a given text (string of nucleotides)

# def most_frequent_kmer(text, k):
#     # Initialize a dictionary to store the kmers and their counts
#     kmer_counts = {}

#     # Loop over the string
#     for i in range(len(text) - k + 1):
#         # Get the current kmer
#         kmer = text[i:i+k]

#         # If the kmer is not in the dictionary, add it with a count of 1
#         if kmer not in kmer_counts:
#             kmer_counts[kmer] = 1
#         # If the kmer is already in the dictionary, increment its count
#         else:
#             kmer_counts[kmer] += 1

#     # Find the kmer with the maximum count
#     max_count = max(kmer_counts.values())
#     most_frequent_kmers = [kmer for kmer, count in kmer_counts.items() if count == max_count]

#     return most_frequent_kmers, max_count

# text = "TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT"
# k = 3

# print(most_frequent_kmer(text, k))

# ---------------------------------------------------------------------------------------------------------------------------------------------
# Check if a chunck of the DNA code is a palindrome
code_1 = "ATTA"
code_2 = code_1[::-1]
if code_1 == code_2:
    print(f"{code_1} is a palindrome.")
else:
    print(f"{code_1} is not a palindrome")
# ---------------------------------------------------------------------------------------------------------------------------------------------
# Work out and print the reverse complement of given
''' Note: The reverse complement of a DNA sequence
is formed by reversing the sequence and then replacing each nucleotide (string of letters) 
with its complement. The complements are A ↔ T and C ↔ G. '''

# Declare the original string of DNA
dna_original = "TTGTGTC"
# Use built in functions to reverse the string
dna_reverse = dna_original[::-1]
# print(dna_reverse) # Print half-way through to check!

# Use built in functions to replace the following pairs of letters: A ↔ T and C ↔ G
dna_complement_T = dna_reverse.replace("T", "A")
# print(dna_complement_T)

dna_complement_G = dna_complement_T.replace("G", "C")
# print(dna_complement_G)

# To change the first 'C' to G without affecting the rest of the 'C's in the string, ude [1:] and concatinate with 'G'
dna_complement_final = 'G' + dna_complement_G[1:]
print(dna_original)
print(dna_complement_final)
# ---------------------------------------------------------------------------------------------------------------------------------------------

replication_origin = "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaac ctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca cggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgactt gtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggatt acgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttagga tagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaat tgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaag atcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtt tccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc"

frequency_of_a = 0
frequency_of_c = 0
frequency_of_g = 0
frequency_of_t = 0 

for i in range(len(replication_origin)) :
    if replication_origin[i] == "a" :
        frequency_of_a += 1
    elif replication_origin[i] == "c" :
        frequency_of_c += 1
    elif replication_origin[i] == "g" :
        frequency_of_g += 1 
    elif replication_origin[i] == "t" :
        frequency_of_t += 1

print(f"Frequency of letter a is", round(frequency_of_a / len(replication_origin) * 100, 1), \
"% .")
print(frequency_of_c)
print(frequency_of_g)
print(frequency_of_t)
#print(replication_origin)
# ---------------------------------------------------------------------------------------------------------------------------------------------
