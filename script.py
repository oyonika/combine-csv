import os
import glob
import pandas as pd

os.chdir("the/directory/with/all/csv/files")

extension = 'csv'
filenames = [i for i in glob.glob('*.{}'.format(extension))]

# Create a list for all .csv file data
csv = pd.concat([pd.read_csv(f) for f in filenames ])

# Export list to CSV
csv.to_csv( "data.csv", index=False, encoding='utf-8-sig')