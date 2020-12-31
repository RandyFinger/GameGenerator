# Game idea generator
import csv
import random

# Read csv
with open('GameIdeas.csv', newline='') as f:
    reader = csv.reader(f)
    
#Print output    
    for row in reader:
        print(row[0] + ':')
        print(row[1] + ':')
        print(row[2] + ':')
        print(row[3] + ':')
        print(row[4] + ':')
        break