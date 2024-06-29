# ChURRO_ABPP

This repository contains the datasets and code used to perform amino acid crowdedness (pPSE) and Ramachandran analyses on prochiral Met oxidation site datasets, using information from predicted protein structures deposited in the [AlphaFold](https://alphafold.ebi.ac.uk/) database.

Paper: (TODO: link to paper)

### Repository Structure

Below is an overview of the folders in this repository as well as brief descriptions of each relevant file in logical order.

- [Mitochondria](#Mitochondria)

- [MsrKD](#MsrKD)

- [Ramachandran-Analysis](#Ramachandran-Analysis)

- [alphafold_data](#alphafold_data)

- [global_data](#global_data)

### Mitochondria

- `Mitochondria_DataSet.xlsx`: Identified prochiral Met oxidation sites in purified mitochondria derived from mouse liver.
- `Mouse.MitoCarta3.0.xls`: The Mouse MitoCarta3.0 dataset from the [Broad Institute](https://www.broadinstitute.org/mitocarta/mitocarta30-inventory-mammalian-mitochondrial-proteins-and-pathways). This is a curated, updated collection of nuclear and mtDNA genes encoding proteins with strong support of mitochondrial localization.
- `datagen-Mitochondria.ipynb`: The code used to calculate the crowdedness (pPSE) for each Met site and generate the two following data files.
- `Mitochondria_peptides_with_alphafold.csv`: The Mitochondria dataset with additional information for Met site identification and pPSE analysis.
- `Mitochondria_mitocarta_with_alphafold.csv`: The Mouse MitoCarta3.0 dataset with additional information for Met site identification and pPSE analysis.

### MsrKD

- `05_10_24_293T_MsrKD_data.xlsx`: Identified prochiral Met oxidation sites in oxidatively-stressed HEK-293T cells with MsrA or MsrB knocked down.
- `datagen-MsrKD.ipynb`: The code used to generate the two following data files.
- `MsrAKD_clean.csv`: The MsrAKD dataset with additional information for Met site identification.
- `MsrB2KD_clean.csv`: The MsrB2KD dataset with additional information for Met site identification.

### Ramachandran-Analysis

- `extraction_of_dihedral_angles.ipynb`: The code used to extract the psi/phi angles from all of the AlphaFold structures stored in [alphafold_data/](/alphafold_data/) to generate the following two data files.
- `MsrAKD_with_PSI_and_PHI.csv`: The MsrAKD dataset, appended with the psi/phi angles of each residue in the dataset.
- `MsrBKD_with_PSI_and_PHI.csv`: The MsrBKD dataset, appended with the psi/phi angles of each residue in the dataset.

### alphafold_data

- `cif/`: The directory with cached AlphaFold structure information (.cif files) for all relevant proteins across all datasets.
- `pae/`: The directory with cached AlphaFold structure information (.pae files) for all relevant proteins across all datasets.

### global_data

- `complete_sequence_cache.csv`: The file where we cache the UniProtID to amino acid sequence mapping for all relevant proteins across all datasets.
- `dihedral_angles.csv`: The file where we cache the psi/phi angles for all residues in all relevant proteins across all datasets.
