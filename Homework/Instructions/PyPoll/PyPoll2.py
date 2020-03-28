import csv
import os

def read_file(path):
    #with open('Resources/election_data.csv') as f:
    with open(path) as f:
        csvreader = csv.reader(f)
        #Printing the first row (the headers)
        #print(next(csvreader))
        #Geting rid of the header
        header = next(csvreader)
        #make a more permanent copy of the dataset (csvreader is the "grocery bag" remember the analogy from sean.. it's just a placeholder to transport the data to a different location)
        data = []
        for row in csvreader:
            data.append(row)
    return data

#Now we have our data stored in the variable "data"
#And we can do work on the dataset now outside of the with open() block

def vote_count(data):
    #Initialize a candidate dictionary
    candidates = {}
    total_votes = 0
    for row in data:
        #These two aren't really necessary
        # voter_id = row[0]
        # county = row[1]
        candidate = row[2]
        total_votes += 1
        if candidate in candidates: #If the next row[2] 'candidate' is inside our dictionary already, add 1 to that candidate's dictionary
            candidates[candidate] += 1
        else: #This is for the first time each candidate shows up in our dictionary candidates
            candidates[candidate] = 1
    return [candidates, total_votes]

# def vote_percents(candidates, total_votes):
#     percents = {}
#     #Loop through the dictionary
#     for candidate, votes in candidates.items():
#         percents[candidate] = round((votes/total_votes)*100,1)
#     return percents

def results(candidates,total_votes):
    winner = ""
    winning_votes = 0
    for candidate, votes in candidates.items():
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes
    print_winner = f"The winner is {winner} with {winning_votes} votes!"
    print_candidates = ""
    for candidate, votes in candidates.items():
        print_candidates = print_candidates + f"{candidate}: {votes} votes ({int(round((votes/total_votes)*100,2))}%)\n" 
    results = f"""{print_winner}
    ----------------------------
    {print_candidates}"""
    return results





data = read_file("Resources/election_data.csv")
candidates, total_votes = vote_count(data)
#percents = vote_percents(candidates,total_votes)
results = results(candidates,total_votes)
print(results)


with open("PyPoll.txt","w") as text_file:
    text_file.write(results)
