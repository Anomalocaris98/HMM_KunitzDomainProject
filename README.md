# Building an HMM for the BPTI/Kunitz Protease Inhibitor Domain

## Project Overview

This repository contains an original implementation of a pipeline for detecting the BPTI/Kunitz-type protease inhibitor domain (Pfam: PF00014) using profile Hidden Markov Models (HMMs). Developed by **Andrea Lenti**, this project integrates structural bioinformatics and sequence-based modeling to distinguish proteins containing the Kunitz domain from those that do not.

The primary goal is to construct and validate a structure-guided HMM and compare its predictive performance with a standard sequence-based HMM built from multiple sequence alignment.

---

## HMMs for Protein Domains

Protein domains like Kunitz often preserve their core structure and functional residues even across distantly related sequences. Profile HMMs model this variability by capturing:

- Conserved residues (emissions)
- Insertions/deletions (gaps)
- Probabilities across positions

By training an HMM on multiple structurally aligned domain instances, we can more accurately detect related proteins—even when sequence identity is low.

---

## Required Tools

Install these via `conda`:

```bash
conda install -c bioconda cd-hit hmmer blast muscle
conda install -c conda-forge biopython
```

| Tool      | Use |
|-----------|-----|
| **CD-HIT**   | Remove redundancy in training sequences |
| **HMMER**    | Build and use HMMs (`hmmbuild`, `hmmsearch`) |
| **BLAST+**   | Identify and filter sequence similarity to prevent overlap |
| **Biopython**| FASTA manipulation via `get_seq.py` |

---

---

## Pipeline Steps

### 0. Extract Representative Kunitz Sequences from PDB
- Use advanced search:
  - Pfam ID: PF00014
  - Resolution ≤ 2.0 Å
  - Sequence length 45–80 amino acids
- Use `cd-hit` to cluster and reduce redundancy:
```bash
cd-hit -i all_kunitz.fasta -o pdb_kunitz_rp.fasta -c 0.95 -n 5
```
### 1. Extract Representative Kunitz Sequences from PDB
---

### 2. Structural Alignment
Use PDBeFold :
- Input: `pdb_kunitz_rp.fasta` (PDB IDs)
- Output: Aligned FASTA file `pdb_kunitz_rp_strali.fasta`

---

### 3. Build HMM from Structural Alignment
```bash
hmmbuild hmm_model/pdb_kunitz_rp_strali.hmm data/alignments/pdb_kunitz_rp_strali.fasta
```

---

### 4. Prepare Benchmark Sets from UniProt
- **Positive set**: All Swiss-Prot entries with PF00014
- **Negative set**: All other Swiss-Prot proteins
- Use `blastpgp` to filter positives with high identity to training set:
```bash
blastpgp -i positives.fasta -d pdb_kunitz_rp.fasta -m 8 -o blast_overlap.txt
```

---

### 5. HMM Search and Cross-Validation
- Split positives/negatives into two folds
- For each fold:
  - Run `hmmsearch`
  - Determine best E-value threshold (based on MCC)
  - Evaluate on held-out fold
```bash
hmmsearch --noali --max --tblout output.tbl -Z 1 --domZ 1 hmm_model/*.hmm test_set.fasta
```

---

### 6. Evaluate Performance
Use the provided script `performance.py` to compute:
- MCC (Matthews Correlation Coefficient)
- Accuracy (Q2)
- True Positive Rate (TPR)
- Precision (PPV)


## Output Files Summary

| File | Description |
|------|-------------|
| `*_strali.hmm` | HMM model from structure-based alignment |
| `*.fasta` | Benchmark sequence sets |
| `*.tbl` | Raw hmmsearch output |
| `*_results.txt` | Performance metrics |
| `*_class` | Binary classification labels (0/1) |

---

## Notes

- You can generate all datasets independently from PDB and UniProt using provided filters.

---

## Author

**Andrea Lenti**  
MSc Bioinformatics – University of Bologna  
Laboratory of Bioinformatics 1 (LB1)

Feel free to open issues or forks for improvements or extensions.

