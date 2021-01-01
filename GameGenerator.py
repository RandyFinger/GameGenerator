# Game idea generator
# Must have pandas installed
import pandas as pd
import random

# Read csv
file = pd.read_csv('GameIdeas.csv')
print(file)

# Print results
# Print column name: print random selection from each column