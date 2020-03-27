##### Come back to this, a lot more can be done to clean, condense, and better automate this code

#Import dependencies
import os
import string
import csv


def PyPoll(data):
    #Initialize some variables
    total_votes = 0
    candidate_voted_for = []
    
    csv = []
    for row in data:
        csv.append(row)

    for row in csv:
        total_votes += 1
        candidate_voted_for.append(row[2])
        #candidate = csv[2]

    #Pull unique elements from the list of candidates voted for
    unique_candidates = set(candidate_voted_for)
    #convert set back to a list
    unique_candidates = list(unique_candidates)

    #Initialize my list of candidate counts based on the index of unique_candidates
    candidate_count = []
    for row in csv:
        #Start the count at 0 for each candidate
        for candidate in unique_candidates:
            candidate_count.append(0)
        #for i in range(len(unique_candidates)):
        for i in range(4):
            if row[2] == unique_candidates[i]:
                #What are we going to do if this is true? add to that index in the candidate_count
                candidate_count[i] += 1

    candidate_1 = unique_candidates[0]
    candidate_2 = unique_candidates[1]
    candidate_3 = unique_candidates[2]
    candidate_4 = unique_candidates[3]

    candidate_1_count = candidate_count[0]
    candidate_2_count = candidate_count[1]
    candidate_3_count = candidate_count[2]
    candidate_4_count = candidate_count[3]     
            
    #percentage votes each candidate won
    #candidate_percentage = []
    # winner = []
    # for i in range(len(unique_candidates)): # or range(len(candidate_count))
    #     #candidate_percentage[i].append(round((int(candidate_count[i])/int(total_votes[i]))*100,2))   #IndexError: list index out of range
    #     #who had the most votes?
    #     if i == 0:
    #         winner = unique_candidates[i]
    #     else: #i = 1,2,3
    #     #elif i == 1 or i == 2 or i == 3:
    #         if candidate_count[i] > winner:
    #             winner = unique_candidates[i]

    #percentages of votes
    candidate_1_per = round((int(candidate_1_count)/int(total_votes))*100,1)
    candidate_2_per = round((int(candidate_2_count)/int(total_votes))*100,1)
    candidate_3_per = round((int(candidate_3_count)/int(total_votes))*100,1)
    candidate_4_per = round((int(candidate_4_count)/int(total_votes))*100,1)

    #Determine the winner
    winner = []
    #Candidate 1 winner scenario:
    if (candidate_1_count > candidate_2_count) and (candidate_1_count > candidate_3_count) and (candidate_1_count > candidate_4_count):
    #Is there a way to write this like "if candidate_1_count > (candidate_2_count and candidate_3_count and candidate_4_count)"?
        winner = candidate_1
    #Candidate 2 winner scenario:
    elif (candidate_2_count > candidate_1_count) and (candidate_2_count > candidate_3_count) and (candidate_2_count > candidate_4_count):
        winner = candidate_2
    #Candidate 3 winner scenario:
    elif (candidate_3_count > candidate_2_count) and (candidate_3_count > candidate_1_count) and (candidate_3_count > candidate_4_count):
        winner = candidate_3


    return [total_votes,candidate_1,candidate_1_count,candidate_1_per,candidate_2,candidate_2_count,candidate_2_per,candidate_3,candidate_3_count,candidate_3_per,candidate_4,candidate_4_count,candidate_4_per,winner]
    

csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #Skip the header line
    header = next(csvreader)
    analysis = PyPoll(csvreader)


print(f"""
Election Results
-----------------
Total Votes: {analysis[0]}
-----------------
{analysis[1]}: {analysis[3]} ({analysis[2]})
{analysis[4]}: {analysis[6]} ({analysis[5]})
{analysis[7]}: {analysis[9]} ({analysis[8]})
{analysis[10]}: {analysis[12]} ({analysis[11]})
-----------------
Winner: {analysis[13]}
""")


with open("PyPoll.txt","w") as text_file:
    text_file.write(f"""
Election Results
-----------------
Total Votes: {analysis[0]}
-----------------
{analysis[1]}: {analysis[3]} ({analysis[2]})
{analysis[4]}: {analysis[6]} ({analysis[5]})
{analysis[7]}: {analysis[9]} ({analysis[8]})
{analysis[10]}: {analysis[12]} ({analysis[11]})
-----------------
Winner: {analysis[13]}
""")
        





