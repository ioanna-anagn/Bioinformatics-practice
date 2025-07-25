# count_nucleotides.py

def count_nucleotides(fasta_file):
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                continue
            for nucleotide in line.strip():
                if nucleotide in counts:
                    counts[nucleotide] += 1
    return counts

# Παράδειγμα χρήσης
if __name__ == "__main__":
    fasta = "example.fasta"
    result = count_nucleotides(fasta)
    print("Nucleotide counts:")
    for base, count in result.items():
        print(f"{base}: {count}")
