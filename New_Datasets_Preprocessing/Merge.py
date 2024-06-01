import pandas as pd
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


def csv_to_fasta(csv_file, fasta_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Iterate over DataFrame rows and extract sequences
    with open(fasta_file, 'a') as fasta_file:
        for index, row in df.iterrows():
            sequence_id = row['ACC']
            sequence = row['Sequence']
            seq_record = SeqRecord(Seq(sequence), id=sequence_id, description="")
            # SeqIO.write(seq_record, fasta_file, "fasta")
            fasta_file.write(f">{seq_record.id}\n{str(seq_record.seq)}\n")


# Example usage
csv_file_path = "Combined_Dataset/deeploc_combined_data_1kclipped.csv"
fasta_file_path = "Final_Datasets/Modified_Dataset_Ex/deeploc_swissprot_clipped1k.fasta"
csv_to_fasta(csv_file_path, fasta_file_path)
