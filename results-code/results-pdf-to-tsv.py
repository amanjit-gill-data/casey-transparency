# convert group A result pdf files to tsv

import os
import sys
import tabula.io

# %% 

DIR = sys.argv[1]

# %% 

def convert_all_pdf() -> None:

    """
    convert all PDFs in given dir to TSV
    store TSVs in same dir as PDFs
    """

    tabula.io.convert_into_by_batch(input_dir=DIR, output_format="tsv", pages=1)

# %% 

def clean_one_tsv(tsv: str) -> None:

    """
    clean given TSV
    """

    with open(tsv, "r") as file:
        lines = file.readlines()
        
    [lines.pop(0) for _ in range(0,6)]
    
    with open(tsv, 'w') as file:
        file.writelines(lines)

# %% 

def clean_all_tsv() -> None:

    """
    clean all TSVs in given dir
    """

    for file in os.listdir(DIR):
        if file.endswith(".tsv"):
            clean_one_tsv(DIR + "/" + file) # filename doesn't include DIR

# %% 

def main():

    convert_all_pdf()
    clean_all_tsv()

# %% 

if __name__ == "__main__":
    main()

