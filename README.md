# ChURRO_ABPP
This repository contains the code used to perform Amino Acid Crowdedness (pPSE) and Ramachandran analyses.

## Repository Structure
Below is an overview of the folders in this repository:

- [MsrKD](#MsrKD)
- [Ramachandran Analysis](#Ramachandran-Analysis)
- [RvsS](#RvsS)
- [alphafold_data](#alphafold_data)
- [global_data](#global_data)

## MsrKD

## Ramachandran Analysis

- [MsrAKD_with_PSI_and_PHI.csv]():The MsrAKD dataset with an additional columns containing the PSI and PHI angles of each residue in the dataset. 
- [MsrBKD_with_PSI_and_PHI.csv]():The MsrBKD dataset with an additional columns containing the PSI and PHI angles of each residue in the dataset. 
- [RvsS_with_PSI_and_PHI.csv](): The RvsS dataset with an additional columns containing the PSI and PHI angles of each residue in the dataset. 
- [dihedral_angles.csv](): CSV file that stores the PSI and PHI angles for all residues across all datasets.
- [extraction_of_dihedral_angles.ipynb](): Contains the code used to extract the PSI and PHI angles from the alphafold structures stored in [alphafold_data](https://stackedit.io/alphafold_data).
## RvsS
- [Mouse.MitoCarta3.0.xls](RvsS/Mouse.MitoCarta3.0.xls): Dataset containing of the mouse mitchondrial proteome.
- [RvsS_DataSet.xlsx](RvsS/RvsS_DataSet.xlsx): 
- [RvsS/RvsS_full_mitochondrial_with_alphafold.csv](RvsS/RvsS/RvsS_full_mitochondrial_with_alphafold.csv):
- [RvsS_peptides_with_alphafold.csv](RvsS/RvsS_peptides_with_alphafold.csv): The RvsS dataset with additional columns that contain the accessibility scores of each residue in the dataset.
- [analysis-RvsS.ipynb](RvsS/analysis-RvsS.ipynb):
- [datagen-RvsS.ipynb](RvsS/datagen-RvsS.ipynb):
## alphafold_data

## global_data
