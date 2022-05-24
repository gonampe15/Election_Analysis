# The data we need
# 1. Total number of votes
# 2. Complete list of candidates
# 3. Votes percentage per candidate
# 4. Total number of votes per candidate
# 5. The winner 

import csv

import os
# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    
    # Read and print the header row
    
    headers = next(file_reader)
    
    print(headers)