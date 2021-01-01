# Game idea generator
# Must have pandas installed
import pandas as pd
import random

# Read csv into dataframe
df = pd.read_csv('GameIdeas.csv')

# Make random selection
environment = random.randint(0, len(df["Environment"]) + 1)
goal = random.randint(0, len(df["Goal"]) + 1)
genre = random.randint(0, len(df["Genre"]) + 1)
rules = random.randint(0, len(df["Rules"]) + 1)
features = random.randint(0, len(df["Extra Features"]) + 1)

# Print results
print("Environment: " + str(df.iat[environment,0]))
print("Goal: " + str(df.iat[goal,1]))
print("Genre: " + str(df.iat[genre,2]))
print("Rules: " + str(df.iat[rules,3]))
print("Extra Features: " + str(df.iat[features,4]))    