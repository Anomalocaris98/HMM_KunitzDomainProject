# BPTI/Kunitz Domain Detection Using Hidden Markov Models (HMM)

# Project Overview
This project implements a computational approach to detect BPTI/Kunitz domains in proteins using Hidden Markov Models (HMMs). It combines structural bioinformatics with probabilistic modeling to identify conserved patterns characteristic of the Kunitz domain.

# Main Goals
- Build an HMM based on structural alignments of known Kunitz domain proteins.
- Scan large protein databases (e.g., UniProt) to identify proteins that contain the domain.
- Evaluate model performance through cross-validation and metrics such as precision, recall, and ROC-AUC.

# Folder Structure
```
BPTI_Kunitz_HMM_Detection/
├── data/                  # Raw and preprocessed input data
│   ├── pdb_structures/    # PDB files and sequences
│   ├── uniprot_sets/      # Positive/negative sets from UniProt
│   └── alignments/        # Structural and sequence alignments
│
├── hmm_model/             # HMMs and search results
│   └── hmm_results/
│
├── scripts/               # Bash/Python scripts for automation
│
├── results/               # Evaluation metrics and plots
│
│
├── README.md              # This file
└── LICENSE
```

# How to Use
1. Prepare PDB sequences and align using a structural tool.
2. Build the HMM using `hmmbuild`.
3. Fetch and clean training/testing sets from UniProt.
4. Run `hmmsearch` and evaluate using provided scripts.

# Requirements
- HMMER (hmmbuild, hmmsearch)
- BLAST+ tools (blastclust, blastpgp)
- Python and Biopython for evaluation

# Author
Andrea Lenti
