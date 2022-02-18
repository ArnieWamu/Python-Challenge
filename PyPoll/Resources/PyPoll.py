# Import modules
import os
import csv

# Set path for file
PyPollcsv = os.path.join("Resources", "election_data.csv")
PyPollcsv = r'C:\Users\arnol\OneDrive\Desktop\Python-Challenge\Instructions\PyPoll\Resources\election_data.csv'
file_to_output = os.path.join("Output", "results.txt")
file_to_output = r'C:\Users\arnol\OneDrive\Desktop\Python-Challenge\Instructions\PyPoll\Resources\Output\results.txt'

# Set variables
total_votes = 0

# Lists to store data
candidates = []
num_votes = []
percent_votes = []

# Open csv file
with open(PyPollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:

        # Total number of votes cast
        total_votes = total_votes + 1

# A complete list of candidates who received votes
# Appending candidate names list
        name_candidate = row[2]
# Condition for if candidate does not match any candidates
        if name_candidate not in candidates:
            candidates.append(name_candidate)
            index = candidates.index(row[2])
            num_votes.append(1)
        else: 
            index = candidates.index(row[2])
            num_votes[index] += 1
# Percentage of votes each candidate won and the total number of votes each candidate won
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

# Winner of the election based on popular vote
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]



# open the output file in write mode
with open(file_to_output,'w') as analysis:
# Print results in terminal
    print("Election Results")
    print("\n----------------------------")
    print(f"\nTotal Votes: {total_votes}")
    print("---------------------------------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    print("\n----------------------------") 
    print(f"\nWinner: {winner}")
    print("\n----------------------------")

