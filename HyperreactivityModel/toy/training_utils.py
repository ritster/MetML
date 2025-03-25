"""
Useful functions for training setup.
"""

import os

import numpy as np
import pandas as pd

from iFeatureOmegaCLI import iProtein


def dataset_to_fasta(peptides: pd.DataFrame, out_file: os.path, window_size: int=20, amino_acid: str="M", analysis_threshold: int=20) -> None:
    """
    Process a DataFrame with ...
    """

    fastas = peptides[["Site", f"Left {analysis_threshold}", f"Right {analysis_threshold}", "Average H/L", "Hyperreactive"]]

    # Filter by hyperreactivity threshold and some accessibility value (TODO)
    fastas = fastas[(fastas["Average H/L"]  <= 2) | (fastas["Average H/L"]  >= 5)]
    # fastas = fastas[fastas["Radius"] <= threshold]

    # Write sequences to fasta file
    n_peptides = 0
    with open(out_file, "wt") as f:
        for index, row in fastas.iterrows():
            k = str(row["Site"]) + "," + str(row["Hyperreactive"])
            v = str(row["Left 20"])[-window_size:] + amino_acid + str(row["Right 20"])[:window_size]
            f.write(f">{k}\n{v}\n")
            n_peptides += 1

    print(f"Wrote {n_peptides} new peptides to {out_file}.")
    return

def BLAST():
    return "asdf"

def CKSAAP(fasta_path: os.path, k: int=5) -> pd.DataFrame:
    """
    Run CKSAAP on the given FASTA file.
    """

    # Write CKSAAP parameters to JSON file
    params = f'{{ "CKSAAP type 1": {{"kspace": {k}}} }}\n'
    with open("./CKSAAP_params.json", "wt") as f:
        f.write(params)

    # Run CKSAAP with given parameters
    features = iProtein(fasta_path)
    features.import_parameters("./CKSAAP_params.json")
    features.get_descriptor("CKSAAP type 1")
    features_df = features.encodings

    # Extract FASTA keys (site, label) into DataFrame
    features_df.index = features_df.index.str.split(',', expand=True)
    features_df.index.names = ["Site", "Hyperreactivity Label"]
    features_df = features_df.reset_index()

    return features_df

def tCKSAAP() -> pd.DataFrame:
    return "goodbye"