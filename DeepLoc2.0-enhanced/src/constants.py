
from src.meta import BASE_DIR

CATEGORIES = ["Membrane","Cytoplasm","Nucleus","Extracellular","Cell membrane","Mitochondrion","Plastid","Endoplasmic reticulum","Lysosome/Vacuole","Golgi apparatus","Peroxisome"]
SS_CATEGORIES = ["NULL", "SP", "TM", "MT", "CH", "TH", "NLS", "NES", "PTS", "GPI"] 

FAST = "Fast"
ACCURATE = "Accurate"
FAST2 = "Fast2"
MAMBA = "Mamba"

EMBEDDINGS = {
    FAST: {
        "embeds": BASE_DIR+"data_files/embeddings/esm1b_swissprot.h5",
        "config": "swissprot_esm1b.yaml",
        "source_fasta": BASE_DIR+"data_files/deeploc_swissprot_clipped1k.fasta"
    },
    FAST2: {
        "embeds": BASE_DIR+"data_files/embeddings/esm2b_swissprot.h5",
        "config": "swissprot_esm2b.yaml",
        "source_fasta": BASE_DIR+"data_files/deeploc_swissprot_clipped1k.fasta"
    },
    MAMBA: {
        "embeds": BASE_DIR+"data_files/embeddings/prott5_swissprot.h5",
        "config": "swissprot_prott5.yaml",
        "source_fasta": BASE_DIR+"data_files/deeploc_swissprot_clipped4k.fasta"
    },
    ACCURATE: {
        "embeds": BASE_DIR+"data_files/embeddings/prott5_swissprot.h5",
        "config": "swissprot_prott5.yaml",
        "source_fasta": BASE_DIR+"data_files/deeploc_swissprot_clipped4k.fasta"
    }
}

SIGNAL_DATA = BASE_DIR+"data_files/multisub_ninesignals.pkl"
LOCALIZATION_DATA = "./data_files/multisub_5_partitions_unique.csv"

BATCH_SIZE = 128
SUP_LOSS_MULT = 0.1
REG_LOSS_MULT = 0.1

