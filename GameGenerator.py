# Game idea generator
# Must have pandas installed
import pandas as pd
import random

# Read csv into dataframe
df = pd.read_csv('GameIdeas.csv')

''' Get actual column count ignoring nan values to make code modular
envCount = 0
goalCount = 0
genreCount = 0
rulesCount = 0
featuresCount = 0
'''

# Make random selection
environment = random.randint(0, 17)
goal = random.randint(0, 11)
genre = random.randint(0, 10)
rules = random.randint(0, 9)
features = random.randint(0, 6)

# Print results
print("Environment: " + str(df.iat[environment,0]))
print("Goal: " + str(df.iat[goal,1]))
print("Genre: " + str(df.iat[genre,2]))
print("Rules: " + str(df.iat[rules,3]))
print("Extra Features: " + str(df.iat[features,4]))    