import pandas as pd
import os
import glob

os.chdir("/home/prakhar/combine_data")

file_extension = '.csv'

all_filenames = [i for i in glob.glob(f"*{file_extension}")]

combined_csv_data = pd.concat([pd.read_csv(f) for f in all_filenames])

combined_csv_data.to_csv("spiderIndiaDataset.csv")
