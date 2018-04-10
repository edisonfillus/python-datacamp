'''
Created on 5 de abr de 2018

@author: Edison Klafke Fillus
'''

import pandas as pd
# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('../../datasets/tweets.csv',chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang'] :
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)
