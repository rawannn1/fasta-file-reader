from Bio import SeqIO

# Replace with your actual file path
fasta_file = "example.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
    print("ID:", record.id)
    print("Sequence:", record.seq)
    print("Length:", len(record.seq))
