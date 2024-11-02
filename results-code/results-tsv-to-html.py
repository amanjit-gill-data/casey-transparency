# convert group A result tsv files to html

import os
import pandas as pd
import sys

# %% 

DIR = sys.argv[1]

# %% 

def main():

    for file in os.listdir(DIR):
        if file.endswith(".tsv"):
            df = pd.read_csv(DIR + "/" + file, sep="\t") # filename doesn't include DIR 
            html_file = file.replace(".tsv", ".html")
            df.to_html(DIR + "/" + html_file, index=False, border=0, justify="unset")

# %% 

if __name__ == "__main__":
    main()

