# Game idea generator
# Must have pandas installed
import pandas as pd
import random

# Read csv into dataframe
df = pd.read_csv('GameIdeas.csv')

# Make random selection
environment = random.randint(1, len(df["Environment"]))
goal = random.randint(1, len(df["Goal"]))
genre = random.randint(1, len(df["Genre"]))
rules = random.randint(1, len(df["Rules"]))
features = random.randint(1, len(df["Extra Features"]))

# Print results
# print("Environment: " + df["Environment"].)
# print("Goal: ")
# print("Genre: ")
# print("Rules: ")
# print("Extra Features: ")    